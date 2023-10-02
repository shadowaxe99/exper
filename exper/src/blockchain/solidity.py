```python
from web3 import Web3
from solcx import compile_source

class SolidityManager:
    def __init__(self, contract_source_code, contract_name):
        self.contract_source_code = contract_source_code
        self.contract_name = contract_name
        self.compiled_sol = compile_source(self.contract_source_code)
        self.contract_interface = self.compiled_sol['<stdin>:' + self.contract_name]

    def deploy_contract(self, web3, account):
        contract = web3.eth.contract(abi=self.contract_interface['abi'], bytecode=self.contract_interface['bin'])
        tx_hash = contract.constructor().transact({'from': account.address})
        tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        return tx_receipt

    def get_contract_instance(self, web3, contract_address):
        contract_instance = web3.eth.contract(
            abi=self.contract_interface['abi'],
            address=contract_address
        )
        return contract_instance

# Connect to local Ethereum node
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Solidity source code for Elysium OS Investor Experience
contract_source_code = '''
pragma solidity ^0.5.0;

contract ElysiumOSInvestorExperience {
    // Contract code goes here
}
'''

# Initialize Solidity manager
solidity_manager = SolidityManager(contract_source_code, 'ElysiumOSInvestorExperience')

# Deploy contract and get contract instance
account = web3.eth.accounts[0]
tx_receipt = solidity_manager.deploy_contract(web3, account)
contract_instance = solidity_manager.get_contract_instance(web3, tx_receipt['contractAddress'])

# Interact with contract
# contract_instance.functions.functionName().call()
```