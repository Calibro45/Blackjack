############### Blackjack Project #####################

import random
import art


def blackjack():
    print(art.logo)

    # Create hands and pick random card for user and pc
    user_cards = []
    user_cards_logo = []
    computer_cards = []
    computer_cards_logo = []
    user_score = 0
    computer_score = 0
    is_game_over = False
    divider = "\n------------------------------"

    def deal_card():
        ''''Pick a random card for list of cards'''
        cards = art.cards_logo
        random_card = random.choice(cards)
        return random_card

    def append_cards(card, cards_list, cards_logo):
        '''Append the value and the logo in the ripective list of card'''
        cards_list.append(card["value"])
        cards_logo.append(card["logo"])

    def show_cards(cards):
        '''Take the list of cards logos and return the logo of the card'''
        cards_logo = ""
        for card in cards:
            cards_logo += card
        return cards_logo

    def calculate_score(cards):
        '''Calc the sum of the list of card for player'''
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def compare(us_score, pc_score):
        ''''Take the score of user and pc, compare them and declare the winner'''
        user_hand = f"Your final hand is: {show_cards(user_cards_logo)}\nwith a score of: {us_score}"
        computer_hand = f"\ncomputer final hand is: {show_cards(computer_cards_logo)}\nwith a score of: {pc_score}"
        end_message = user_hand + divider + computer_hand

        if us_score == pc_score:
            if pc_score == 0:
                return end_message + divider + "\nYou lose the Dealer hit the Blackjack"
            else:
                return end_message + divider + "\nIt's a draw"
        elif pc_score == 0:
            return end_message + divider + "\nYou lose the Dealer hit the Blackjack"
        elif us_score == 0:
            return end_message + divider + "\nYou win with a Blackjack"
        elif us_score > 21:
            return end_message + divider + "\nYou lose: you are out of range"
        elif pc_score > 21:
            return end_message + divider + "\nYou win: the Dealer are out of range"
        elif us_score > pc_score:
            return end_message + divider + "\nYou win with a max score"
        else:
            return end_message + divider + "\nYou lose the Dealer have a max score"

    for _ in range(2):
        user_card = deal_card()
        computer_card = deal_card()

        append_cards(user_card, user_cards, user_cards_logo)
        append_cards(computer_card, computer_cards, computer_cards_logo)

    while not is_game_over:
        # Calculating the score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards:{show_cards(user_cards_logo)}\ncurrent score: {user_score}")
        print(divider)
        print(f"computer first card is: {computer_cards_logo[0]}")

        # Check the score for end game
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            new_card = input("you want to draw another card? Type 'y' or 'n'. ").lower()
            if new_card == "y":
                print(divider)
                user_card = deal_card()
                append_cards(user_card, user_cards, user_cards_logo)
            else:
                is_game_over = True

    # Computer turn for draw card
    while computer_score != 0 and computer_score < 17:
        computer_card = deal_card()
        append_cards(computer_card, computer_cards, computer_cards_logo)

        computer_score = calculate_score(computer_cards)

    # Compare the score with the compare function and show the winnner
    print(divider)
    game_over = compare(user_score, computer_score)
    print(game_over)

    # Ask for play new game
    print(divider)
    play_again = input("Do you want to play again? Type 'y' or 'n'.").lower()

    if play_again == "y":
        print("\n" * 80)
        blackjack()
    else:
        print("Game Over")


# Start the game once
play = input("Do you want play Blackjack? Type 'y' or 'n':  ").lower()
if play == "y":
    blackjack()
else:
    print("Bye")