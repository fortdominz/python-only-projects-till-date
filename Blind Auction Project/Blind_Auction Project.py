import blind_auction_art
print(blind_auction_art.logo)

# TODO-1: Ask the user for input

# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary

def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner}, with a bid of ${highest_bid}.")


bids = {}  # if put inside the loop, accumulated data will be lost when the loop runs

continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("How much do you want to bid? $"))
    bids[name] = price
    next_bidder = input("Are there any other bidders? Type 'yes' for yes or 'no' for no. \n").lower()

    if next_bidder == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    elif next_bidder == 'yes':
        print("\n" * 200)
        continue
