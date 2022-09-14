from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program")


def add_bid_info(bidder_name, bidder_bidding):
	bid_dict[bidder_name] = bidder_bidding


def calc_bid(dict):
	max_list = []
	max_value = 0
	for key, value in dict.items():
		if value > max_value:
			max_list = []
			max_value = value
			max_list.append([key, value])

# max_value와 같은 값을 입력했을 경우
		elif max_value == value:
			max_list.append([key, value])

	winner = ""
	winner_bidding = ""
	for i in max_list:
		winner += f"{i[0]}, "
		winner_bidding = i[1]

	return winner, winner_bidding

bid_dict = {}
bid_again = True

while bid_again:
	bidder_name = input("What is your name?: ")
	bidder_bidding = int(input("What's your bid?: $"))
	add_bid_info(bidder_name, bidder_bidding)
	other_bidder = input(
	    "Are there any other bidders? Type 'yes' or 'no'.\n").lower()
	if other_bidder != "yes":
		bid_again = False
		winner, winner_bidding = calc_bid(bid_dict)
		print(
		    "================================================================="
		)
		print(f"The winner is {winner} with a bid of ${winner_bidding}")
	else:
		clear()
