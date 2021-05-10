from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

bids = {}
bidding_is_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner =""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid ${highest_bid}")


while not bidding_is_finished:
  name = input("what's your name?")
  price = int(input("what's the bid? $ "))
  bids[name] = price
  should_countinue=input("Are any other bidders? type 'yes' or 'no'.\n")
  if should_countinue == "no":
    bidding_is_finished = True
    find_highest_bidder(bids)
  elif should_countinue == "yes":
    clear()

