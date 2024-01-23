import random

class Card:
    def __init__(self, card_type, number, color):
        self.type = card_type
        self.number = number
        self.color = color

def create_deck():
    card_types = ["Rock", "Paper", "Scissors"]
    colors = ["Red", "Blue", "Yellow", "Green", "Orange"]

    deck = []

    for card_type in card_types:
        for color in colors:
            for _ in range(3):
                number = random.randint(2, 7)
                card = Card(card_type, number, color)
                deck.append(card)

    # Assign a number between 2 and 7 to 18 cards randomly
    for _ in range(18):
        random_card = random.choice(deck)
        random_card.number = random.randint(2, 7)

    # Assign special numbers 8, 9, and 10 to 1 random card each
    for special_number in [8, 9, 10]:
        special_card = random.choice(deck)
        special_card.number = special_number

    # Shuffle the deck
    random.shuffle(deck)

    return deck

def draw_initial_cards(deck, num_cards):
    return random.sample(deck, num_cards)

def draw_new_card(deck):
    return deck.pop(0)

def print_deck_list(player_deck, player_num):
    print(f"\nPlayer {player_num}'s Initial Deck:")
    for i, card in enumerate(player_deck, start=1):
        print(f"{i}. {card.type} - {card.number} - {card.color}")

def print_player_hand(player_deck):
    print("\nYour Hand:")
    for i, card in enumerate(player_deck, start=1):
        print(f"{i}. {card.type} - {card.number} - {card.color}")

def play_round(player_deck, opponent_deck, win_pile, deck, round_num):
    print(f"\nRound {round_num} - Drawing a Card for Each Player")

    # Draw a card for each player at the start of each round (except the first round)
    if round_num > 1:
        if len(player_deck) < 5:
            player_deck.append(draw_new_card(deck))
        if len(opponent_deck) < 5:
            opponent_deck.append(draw_new_card(deck))

    print_player_hand(player_deck)
    player_choice = int(input("Select a card by entering its number: ")) - 1

    print(f"\nYou played: {player_deck[player_choice].type} - {player_deck[player_choice].number} - {player_deck[player_choice].color}")
    print(f"Opponent played: {opponent_deck[0].type} - {opponent_deck[0].number} - {opponent_deck[0].color}")

    if player_deck[player_choice].type == opponent_deck[0].type:
        # Handle tie
        if player_deck[player_choice].number > opponent_deck[0].number:
            print("You win this round!")
            win_pile.append(player_deck[player_choice])  # Add player's card to win pile
            win_pile.append(opponent_deck[0])  # Add opponent's card to win pile
        elif player_deck[player_choice].number < opponent_deck[0].number:
            print("Opponent wins this round! Discarding your card.")
            player_deck.pop(player_choice)
        else:
            print("It's a tie for this round! No one wins.")
    else:
        # Handle non-tie scenarios
        if (player_deck[player_choice].type == "Rock" and opponent_deck[0].type == "Scissors") or \
           (player_deck[player_choice].type == "Scissors" and opponent_deck[0].type == "Paper") or \
           (player_deck[player_choice].type == "Paper" and opponent_deck[0].type == "Rock"):
            print("You win this round!")
            win_pile.append(player_deck[player_choice])  # Add player's card to win pile
            player_deck.pop(player_choice)  # Discard opponent's card
        else:
            print("Opponent wins this round! Discarding your card.")
            player_deck.pop(player_choice)

def check_winning_conditions(win_pile):
    rock_colors = set()
    paper_colors = set()
    scissors_colors = set()

    for card in win_pile:
        if card.type == "Rock":
            rock_colors.add(card.color)
        elif card.type == "Paper":
            paper_colors.add(card.color)
        elif card.type == "Scissors":
            scissors_colors.add(card.color)

    # Check if a player has won based on the updated winning conditions
    if (len(rock_colors) >= 1 and len(paper_colors) >= 1 and len(scissors_colors) >= 1) or \
       (len(rock_colors) >= 3 or len(paper_colors) >= 3 or len(scissors_colors) >= 3):
        return True

    return False

def print_winner_win_pile(winner_win_pile):
    print("\nWinner's Win Pile:")
    for card in winner_win_pile:
        print(f"{card.type} - {card.number} - {card.color}")

def main():
    deck = create_deck()

    # Assuming two players
    player1_deck = draw_initial_cards(deck, 5)
    player2_deck = draw_initial_cards(deck, 5)

    # Print initial deck list for both players
    print_deck_list(player1_deck, 1)
    print_deck_list(player2_deck, 2)

    win_pile = []

    round_num = 1

    while not check_winning_conditions(win_pile):
        print(f"\nPlayer 1's Turn (Round {round_num}):")
        play_round(player1_deck, player2_deck, win_pile, deck, round_num)

        if check_winning_conditions(win_pile):
            break

        print(f"\nPlayer 2's Turn (Round {round_num}):")
        play_round(player2_deck, player1_deck, win_pile, deck, round_num)

        round_num += 1

    print("\nGame Over! A player has met the winning conditions.")
    
    # Determine the winner (you can modify this based on your winning conditions)
    winner = "Player 1" if check_winning_conditions(win_pile[:3]) else "Player 2"
    
    if winner == "Player 1":
        print_winner_win_pile(win_pile[:3])
    else:
        print_winner_win_pile(win_pile[3:])

if __name__ == "__main__":
    main()
