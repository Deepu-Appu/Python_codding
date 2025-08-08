from art9 import logo

print(logo)

# Save data into dictionary {name: price}
bids = {}
continue_bidding = True

# Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    #other method
    # winner = max(bidding_dictionary, key=bidding_dictionary.get)
    # highest_bid = bidding_dictionary[winner]

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while continue_bidding:
    # Ask the user for inputs
    name = input("what is your name?:\n")
    price = int(input("what is your bid?: \n $ "))
    bids[name] = price
   # Whether if new bids needs to be added
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)


