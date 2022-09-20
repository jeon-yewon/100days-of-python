import random
import art
import replit

def pop_cards(how_many, which_list, card_list):
    for i in range(0, how_many):
        keys = []
        values = []

        for key, value in card_list.items():
            keys.append(key)
            values.append(value)
        #Choose symbol
        rand_int_symbol = random.randint(0, 3)
        symbol_logo = values[rand_int_symbol]["logo"]

        #Choose cardnumber
        rand_int_number = random.randint(
            0,
            len(values[rand_int_symbol]["cards"]) - 1)
        pop_number = values[rand_int_symbol]["cards"].pop(rand_int_number)

        which_list.append([symbol_logo, pop_number])

def print_cards(which_list):
    print_cards = ""
    for i in which_list:
        print_cards += f"[{i[0]} {i[1]}] "

    return print_cards

def calc_score(which_list):
    sum_score = 0
    for i in which_list:
        card_number = i[1]
        letters_10 = ["J", "Q", "K"]
        letters_11 = ["A"]
        if card_number in letters_10:
            sum_score += 10
        elif card_number in letters_11:
            sum_score += 11
        else:
            sum_score += i[1]
    return sum_score


def check_result(your_score, computer_score):
    status = ""
    if your_score > 21:
        status = "lose_bust"
    elif your_score == 21:
        if computer_score == 21:
            status = "draw"
        else:
            status = "win"
    elif your_score == computer_score:
        status = "draw"
    elif computer_score > 21:
        status = "win_bust"
    else:
        #check which score is close to 21
        your_abs = abs(your_score - 21)
        computer_abs = abs(computer_score - 21)
        if your_abs > computer_abs:
            status = "lose"
        else:
            status = "win"

    return status

def print_result(win_status):
    if win_status == "win":
        print("You win 😃")
    elif win_status == "win_bust":
        print("Opponent went over. You win 😁")
    elif win_status == "draw":
        print("Draw 🙃")
    elif win_status == "lose":
        print("You lose 😤")
    elif win_status == "lose_bust":
        print("You went over. You lose 😤")
        

start_game = True
while start_game:
    run_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if run_game == "y":
        replit.clear()
        print(art.logo)
        card_list = {
            "heart": {
                "logo": "♥️",
                "cards": ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
            },
            "diamond": {
                "logo": "♦️",
                "cards": ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
            },
            "clover": {
                "logo": "♣️",
                "cards": ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
            },
            "spade": {
                "logo": "♠️",
                "cards": ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"],
            }
        }
        
        your_cards = []
        computer_cards = []
    
        #pop 2 cards from card_list
        pop_cards(2, your_cards, card_list)
        pop_cards(2, computer_cards, card_list)
        
        #status variable : clear to see
        your_status = print_cards(your_cards)
        computer_status = print_cards(computer_cards)

        #calculate current score
        your_score = calc_score(your_cards)
        computer_score = calc_score(computer_cards)
        
        print(f" 👉 Your cards: {your_status}, current score: {your_score}")
        print(f" 👉 Computer's first card: {computer_status[:7]}")

        #add one more cards section
        should_continue = True
        while should_continue:
            continue_game = input("Type 'y' to get another card, type 'n' to pass: ")

            if continue_game == "y":
                pop_cards(1, your_cards, card_list)

                #computer adds one more cards section
                if computer_score <= 16:
                    pop_cards(1, computer_cards, card_list)
                else:
                    pass

                #update score
                your_score = calc_score(your_cards)
                computer_score = calc_score(computer_cards)

                #update status
                your_status = print_cards(your_cards)
                computer_status = print_cards(computer_cards)

                if your_score >= 21:
                    win_status = check_result(your_score, computer_score)
                    print(f" 👉 Your cards: {your_status}, current score: {your_score}")
                    print(f" 👉 Computer's final hand: {computer_status}, final score: {computer_score}")
                    print("="*30)
                    print_result(win_status)
                    should_continue = False
                else:
                    #print current score
                    print(f" 👉 Your cards: {your_status}, current score: {your_score}")
                    print(f" 👉 Computer's first card: {computer_status[:7]}")
                    #should_continue = True
                    
            else:
                #update score
                your_score = calc_score(your_cards)
                computer_score = calc_score(computer_cards)

                #update status
                your_status = print_cards(your_cards)
                computer_status = print_cards(computer_cards)
                
                win_status = check_result(your_score, computer_score)
                print(f" 👉 Your final hand: {your_status}, final score: {your_score}")
                print(f" 👉 Computer's final hand: {computer_status}, final score: {computer_score}")
                print("="*30)
                print_result(win_status)                
                
                should_continue = False
        
    else:
        start_game = False