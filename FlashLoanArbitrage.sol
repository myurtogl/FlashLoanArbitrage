// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;

import "https://github.com/aave/aave-v3-core/blob/master/contracts/flashloan/base/FlashLoanSimpleReceiverBase.sol";
import "https://github.com/aave/aave-v3-core/blob/master/contracts/interfaces/IPoolAddressesProvider.sol";
import "https://github.com/aave/aave-v3-core/blob/master/contracts/dependencies/openzeppelin/contracts/IERC20.sol";

interface ICPAMM {
    function swap(address _tokenIn, uint _amountIn) external returns (uint amountOut);
    function addLiquidity(uint _amount0, uint _amount1) external returns (uint shares);
    function removeLiquidity(uint _shares) external returns (uint amount0, uint amount1);
    function balanceOf(address account) external view returns (uint);
}

contract SimpleFlashLoan is FlashLoanSimpleReceiverBase {
    address payable owner;

// CPAMM contracts for each trading pair
address public cpamm1Address = 0xB634e543F94e155d185EB27b61E6AA40b116a2Df; // address of CPAMM contract for USDC/WBTC
address public cpamm2Address = 0x4304B373A207156CEE82816b21d82605F6aA2F10; // address of CPAMM contract for LINK/WBTC
address public cpamm3Address = 0x8e9A1928D5F20c794B584667c0a797b5e409219E; // address of CPAMM contract for LINK/USDC
ICPAMM public cpamm1 = ICPAMM(cpamm1Address);
ICPAMM public cpamm2 = ICPAMM(cpamm2Address);
ICPAMM public cpamm3 = ICPAMM(cpamm3Address);
bool path = true;

constructor(address _addressProvider)
    FlashLoanSimpleReceiverBase(IPoolAddressesProvider(_addressProvider))
{
}

function fn_RequestFlashLoan(address _token, uint256 _amount, bool _path) public {
    address receiverAddress = address(this);
    address asset = _token;
    uint256 amount = _amount;
    bytes memory params = "";
    uint16 referralCode = 0;
    path = _path;

    POOL.flashLoanSimple(
        receiverAddress,
        asset,
        amount,
        params,
        referralCode
    );
}

// This function is called after your contract has received the flash loaned amount
function executeOperation(
    address asset,
    uint256 amount,
    uint256 premium,
    address initiator,
    bytes calldata params
) external override returns (bool) {
    address USDC_address = 0xda9d4f9b69ac6C22e444eD9aF0CfC043b7a7f53f;
    address LINK_address = 0x779877A7B0D9E8603169DdbD7836e478b4624789;
    address WBTC_address = 0xf864F011C5A97fD8Da79baEd78ba77b47112935a;
    uint256 MAX_UINT256 = 2**256 - 1;
    if (asset == USDC_address){
        if (path == true){
            IERC20(USDC_address).approve(address(cpamm1), MAX_UINT256);
            IERC20(WBTC_address).approve(address(cpamm2), MAX_UINT256);
            IERC20(LINK_address).approve(address(cpamm3), MAX_UINT256);
            uint256 wbtcAmount = cpamm1.swap(USDC_address, amount);
            uint256 linkAmount = cpamm2.swap(WBTC_address, wbtcAmount);
            uint256 usdcAmount = cpamm3.swap(LINK_address, linkAmount);

            // Paying the loan back.
            uint256 totalAmount = amount + premium;
            IERC20(asset).approve(address(POOL), totalAmount);
            return true;
            }
        else if (path == false){
            IERC20(USDC_address).approve(address(cpamm3), MAX_UINT256);
            IERC20(LINK_address).approve(address(cpamm2), MAX_UINT256);
            IERC20(WBTC_address).approve(address(cpamm1), MAX_UINT256);
            uint256 linkAmount = cpamm3.swap(USDC_address, amount);
            uint256 wbtcAmount = cpamm2.swap(LINK_address, linkAmount);
            uint256 usdcAmount = cpamm1.swap(WBTC_address, wbtcAmount);

            // Paying the loan back.
            uint256 totalAmount = amount + premium;
            IERC20(asset).approve(address(POOL), totalAmount);
            return true;
            }
        }
    else if (asset == WBTC_address){
        if (path == true){
            IERC20(WBTC_address).approve(address(cpamm1), MAX_UINT256);
            IERC20(USDC_address).approve(address(cpamm3), MAX_UINT256);
            IERC20(LINK_address).approve(address(cpamm2), MAX_UINT256);
            uint256 usdcAmount = cpamm1.swap(WBTC_address, amount);
            uint256 linkAmount = cpamm3.swap(USDC_address, usdcAmount);
            uint256 wbtcAmount = cpamm2.swap(LINK_address, linkAmount);

            // Paying the loan back.
            uint256 totalAmount = amount + premium;
            IERC20(asset).approve(address(POOL), totalAmount);
            return true;
            }
        else if (path == false){
            IERC20(WBTC_address).approve(address(cpamm2), MAX_UINT256);
            IERC20(LINK_address).approve(address(cpamm3), MAX_UINT256);
            IERC20(USDC_address).approve(address(cpamm1), MAX_UINT256);

            uint256 linkAmount = cpamm2.swap(WBTC_address, amount);
            uint256 usdcAmount = cpamm3.swap(LINK_address, linkAmount);
            uint256 wbtcAmount = cpamm1.swap(USDC_address, usdcAmount);

            // Paying the loan back.
            uint256 totalAmount = amount + premium;
            IERC20(asset).approve(address(POOL), totalAmount);
            return true;
            }
        }
    }

    function getBalance(address _tokenAddress) external view returns (uint256) {
        return IERC20(_tokenAddress).balanceOf(address(this));
    }
}
