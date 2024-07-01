logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                      .-------------.
                      /_______________\\
'''
print(logo)
bids={}
bidding_finished=False

def highest_bid():
    if not bids:
        print("There are no bids.")
    else:
        highest_bidder = max(bids, key=bids.get)
        print(f"Highest bid is {bids[highest_bidder]}")
        print(f"and the bid goes to {highest_bidder}")

while not bidding_finished:
    name=input("What is your name? ")
    price=int(input("Enter your bid: $"))
    bids[name]=price
    should_continue=input("Any more bids 'yes' or 'no' ").lower()
    if should_continue=="no":
        bidding_finished=True
    elif should_continue=="yes":
        bidding_finished=False
if bidding_finished:
    highest_bid()