from auction_logo import logo

print(logo)
print('Welcome to the secret auction program')

bidders = {}
bidding_finished = False


def find_highest_bidder(bidder):
    highest_bid = 0
    winner = ""
    for i in bidder:
        bid_amount = bidder[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input('What is your name? ')
    bid = int(input('What is your bid? $'))

    bidders[name] = bid

    should_continue = input('are there any other bidder? yes or no? ').lower()

    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bidders)
