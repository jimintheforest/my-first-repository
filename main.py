class Transaction:
    def __init__(self, currency, amount, exchange_rate):
        self.currency = currency
        self.amount = amount
        self.exchange_rate = exchange_rate


def user_input():
    currency = input("Enter the currency: ")
    amount = input("Enter the amount: ")
    exchange_rate = input("Enter the exchange rate: ")
    return Transaction(currency, amount, exchange_rate)


new_transaction = user_input()

print(new_transaction.currency, new_transaction.amount, new_transaction.exchange_rate)

transaction_list = []


def add_transaction():
    transaction = new_transaction
    return transaction_list.append(transaction)


add_transaction()

print(transaction_list)

#test commit
