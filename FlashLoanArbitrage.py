from web3 import Web3
import time

alchemy_url = "your_alchemy_url"
web3 = Web3(Web3.HTTPProvider(alchemy_url))
print(web3.is_connected())

arbitrage_account = 'addressForTheAccount'
key = 'your_private_key'
USDC = '0xda9d4f9b69ac6C22e444eD9aF0CfC043b7a7f53f'
LINK = '0x779877A7B0D9E8603169DdbD7836e478b4624789'
WBTC = '0xf864F011C5A97fD8Da79baEd78ba77b47112935a'

contract_address = "Flash_Loan_contract_address"
abi =[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "asset",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "premium",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "initiator",
				"type": "address"
			},
			{
				"internalType": "bytes",
				"name": "params",
				"type": "bytes"
			}
		],
		"name": "executeOperation",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_token",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "_amount",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "_path",
				"type": "bool"
			}
		],
		"name": "fn_RequestFlashLoan",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_addressProvider",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "ADDRESSES_PROVIDER",
		"outputs": [
			{
				"internalType": "contract IPoolAddressesProvider",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "cpamm1",
		"outputs": [
			{
				"internalType": "contract ICPAMM",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "cpamm1Address",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "cpamm2",
		"outputs": [
			{
				"internalType": "contract ICPAMM",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "cpamm2Address",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "cpamm3",
		"outputs": [
			{
				"internalType": "contract ICPAMM",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "cpamm3Address",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_tokenAddress",
				"type": "address"
			}
		],
		"name": "getBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "POOL",
		"outputs": [
			{
				"internalType": "contract IPool",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

dex_abi = [{"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"_amount0","type":"uint256"},{"internalType":"uint256","name":"_amount1","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"shares","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_shares","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"reserve0","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"reserve1","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_tokenIn","type":"address"},{"internalType":"uint256","name":"_amountIn","type":"uint256"}],"name":"swap","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"token0","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"token1","outputs":[{"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]
dex_addresses = [
    "0xB634e543F94e155d185EB27b61E6AA40b116a2Df", # CPAMM contract for USDC/WBTC
    "0x4304B373A207156CEE82816b21d82605F6aA2F10", # CPAMM contract for WBTC/LINK
    "0x8e9A1928D5F20c794B584667c0a797b5e409219E" # CPAMM contract for LINK/USDC
]
dex_contracts = [web3.eth.contract(address=address, abi=dex_abi) for address in dex_addresses]

FlashLoan = web3.eth.contract(address=contract_address, abi=abi)

def find_arbitrage_opportunity():
    asset = ''
    path = True
    dex_reserves = []
    decimals = [6, 8, 8, 18, 18, 6]
    reserves = []

    for dex in dex_contracts:
        reserve0 = dex.functions.reserve0().call()
        reserve1 = dex.functions.reserve1().call()
        print("reserve0:", reserve0)
        print("reserve1:", reserve1)
        dex_reserves.append(reserve0)
        dex_reserves.append(reserve1)

    for i in range(len(dex_reserves)):
        reserves.append(dex_reserves[i] / 10**decimals[i])

    exchange_rates = [
        reserves[0] / reserves[1],
        reserves[2] / reserves[3],
        reserves[4] / reserves[5],
    ]

    paths = [
        exchange_rates[0] * exchange_rates[1] * exchange_rates[2],
        1/exchange_rates[2] * 1/exchange_rates[1] * 1/exchange_rates[0],
        1/exchange_rates[0] * 1/exchange_rates[2] * 1/exchange_rates[1],
        exchange_rates[1] * exchange_rates[2] * exchange_rates[0]
    ]
    print('Exchange rates on paths: ', paths)
    max_path = min(paths)
    index = paths.index(max_path)
    print('Max profitable path: ', index)
    if max_path < 1:
        if index == 0:
            asset = USDC
            path = True
        elif index == 1:
            asset = USDC
            path = False
        elif index == 2:
            asset = WBTC
            path = True
        elif index == 3:
             asset = WBTC
             path = False
    print('The asset address: ',asset, 'Which way is it: ', path)
    return (asset, path)

def execute_arbitrage(token_address, amount, path):

	if token_address == USDC:
		amount *= 10**6
		print('Flash Loan Amount:', amount)
	if token_address == LINK:
		amount *= 10**18
		print('Flash Loan Amount:', amount)
	if token_address == WBTC:
		amount *= 10**8
		print('Flash Loan Amount:', amount)

	transaction = {
		'from': arbitrage_account,
		'nonce': web3.eth.get_transaction_count(arbitrage_account),
		'gas': 1000000,
		'gasPrice': web3.to_wei('20', 'gwei'),
		'to': contract_address,
		'value': 0,
		'data': FlashLoan.encodeABI(fn_name='fn_RequestFlashLoan', args=[token_address, amount, path])
	}

	signed_transaction = web3.eth.account.sign_transaction(transaction, key)

	transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
	print(f"Transaction hash: {transaction_hash.hex()}")

	transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)
	print("Transaction mined.")

def run_arbitrage_bot():
    while True:
        asset, path = find_arbitrage_opportunity()
        amount = 1
        if asset != '':
            print(f"Arbitrage opportunity found!")

            execute_arbitrage(asset, amount, path)
            print(f"Arbitrage executed.")
        else:
            print("No arbitrage opportunity found.")
        print("Looking for new arbitrage opportunities.")
        time.sleep(45)
#the driver function
run_arbitrage_bot()
