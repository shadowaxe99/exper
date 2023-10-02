```python
from web3 import Web3
from eth_account import Account

class Ethereum:
    def __init__(self, provider_url):
        self.web3 = Web3(Web3.HTTPProvider(provider_url))

    def create_account(self):
        account = Account.create()
        return account.address, account.privateKey

    def get_balance(self, address):
        balance = self.web3.eth.getBalance(address)
        return self.web3.fromWei(balance, 'ether')

    def send_transaction(self, sender_private_key, recipient_address, amount):
        sender_account = Account.privateKeyToAccount(sender_private_key)
        nonce = self.web3.eth.getTransactionCount(sender_account.address)
        gas_price = self.web3.eth.gasPrice
        value = self.web3.toWei(amount, 'ether')
        transaction = {
            'nonce': nonce,
            'gasPrice': gas_price,
            'gas': 21000,
            'to': recipient_address,
            'value': value
        }
        signed_transaction = self.web3.eth.account.signTransaction(transaction, sender_private_key)
        transaction_hash = self.web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
        return transaction_hash.hex()

ethereum = Ethereum('https://mainnet.infura.io/v3/YOUR-PROJECT-ID')
```