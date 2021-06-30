from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

from_address = '0x856F87F012d22a2D926858BDF90E033619f25fdD'
to_address = '0x3F96afa73cb22410e0833bF54ad13a0043d7A86c'
private_key = 'bb61b8521b079e05fcf58c48277fce7eb364ee131d7e555ffcf7fcf711723b4c'

nonce = web3.eth.get_transaction_count(from_address)

tx = {
    'nonce': nonce,
    'to': to_address,
    'value': web3.toWei(1, 'ether'),
    'gas': 21000,
    'gasPrice': web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))