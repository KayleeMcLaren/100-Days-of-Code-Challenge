
#  please run this code on https://replit.com/~ to use the clear() function


from replit import clear
from art import logo

end_of_auction = False
bids = {}

print(logo)

def highest_bidder(list_of_bids):
  highest_bid = 0
  winner_name = ""
  for name in list_of_bids:
    bid_price = list_of_bids[name]
    if bid_price > highest_bid:
      highest_bid = bid_price
      winner_name = name
  print(f"The winner is {winner_name} with a bid of ${highest_bid}.")


while not end_of_auction:
  name = input("What is your name?\n")
  bid_price = int(input("What is your bid?\n$"))
  another_bid = input("Are there any other bidders? Type 'yes' or 'no'?\n")

  bids[name] = bid_price
  highest_bid = bids[name]
  
  if another_bid == 'yes':
    clear()
  else:
    end_of_auction = True
    highest_bidder(bids)
    
