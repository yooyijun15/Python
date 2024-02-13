from replit import clear
from art import logo
print(logo)
print("Welcome to the secret auction program.")

bidders = []

def check_bidder(name, bid):
  winner_name = ""
  winner_bid = 0
  for i in range(0, len(bidders)):
    tmp = bidders[i]["bid"]
    if tmp > winner_bid:
      winner_bid = tmp
      winner_name = bidders[i]["name"]
  print(f"The winner is {winner_name} with a bid of ${winner_bid}")

def add_bidder(name, bid):
  bidders.append(
    {
      "name": name,
      "bid": bid
    }
  )

while True:
  input_name = input("What is your name?: ")
  input_bid = int(input("What is your bid?: $"))
  add_bidder(name = input_name, bid = input_bid)
  check_bidder(name = input_name, bid = input_bid)
  again = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()
  if not again == "yes":
    check_bidder(name = input_name, bid = input_bid)
    break
