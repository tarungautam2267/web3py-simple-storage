from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
install_solc("0.6.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.soureMap"]}
            }
        },
    },
    solc_version="0.6.0",
)
with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/785d3127a7e2484891f60a0fedbcffbe"))
chain_id=4
my_address="0x352E62b2F941962a443d993AeF51fCB496CDbcAD"
private_key="0x72689b230aa9e26209dd73d4a4de22861e889c9f1db9765c9eba29782eab6a37"
SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)

nonce=w3.eth.getTransactionCount(my_address)

transaction = SimpleStorage.constructor().buildTransaction({"gasPrice": w3.eth.gas_price,"chainId": chain_id, "from": my_address, "nonce":   nonce})

signed_txn=w3.eth.account.sign_transaction(transaction, private_key=private_key)

tx_hash=w3.eth.send_raw_transaction(signed_txn.rawTransaction)

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("deployed")
