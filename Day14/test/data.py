from game_data import data
import random

def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."

account_a = random.choice(data)
account_b = random.choice(data)

print(f"{format_data(account_a)}")
print(f"{format_data(account_b)}")
