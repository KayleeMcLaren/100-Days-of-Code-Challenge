
#Please run this code on https://replit.com/~ in order to use the clear() function

import random
from replit import clear
from black_jack_art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # assumes infinite deck, no cards are removed when they're been drawn.
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    """Takes a list of cards and returns the score calculated from the cards"""
    if len(card_list) == 2 and sum(card_list) == 21:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(player_score, dealer_score):
    """Compares player and dealer scores and determines who wins"""
    if player_score > 21 and dealer_score > 21:
        return "You went over, you lose!"
    if player_score == dealer_score:
        return "\nYou draw"
    elif dealer_score == 0:
        return "\nYou lose, dealer has Blackjack!"
    elif player_score == 0:
        return "\nYou win with Blackjack!"
    elif player_score > 21:
        return "\nYou went over, you lose!"
    elif dealer_score > 21:
        return "\nDealer went over, you win!"
    elif player_score > dealer_score:
        return "\nYou Win!"
    else:
        return "\nYou lose!"


def play_blackjack():
    """Game starts here"""
    print(logo)

    player_cards = []
    dealer_cards = []
    game_continue = True
	
  """Deals two cards to the dealer and player"""
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

        """Claculates the scores and reveals the dealer's first card to the player"""
    while game_continue:
        dealer_score = calculate_score(dealer_cards)
        player_score = calculate_score(player_cards)
        print(f"\nDealer's first card: {dealer_cards[0]}")
        print(f"User cards: {player_cards}, score: {player_score}")

        """The player's turn:
        If the dealer or the player have a score of 0 or if the player's score is over 21 the game ends"""
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_continue = False
        else:
            another_card = input("\nWould you like to draw another card? Type 'y' or 'n': ")
            if another_card == 'y':
                player_cards.append(deal_card())
            else:
                game_continue = False

     """The dealer's turn:"""
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"\nThe dealer's final hand is: {dealer_cards}, final score: {dealer_score}")
    print(f"Your final hand is: {player_cards}, final score: {player_score}")
    print(compare(player_score, dealer_score))

"""The game will restart until the player inputs 'n' for no"""
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_blackjack()
