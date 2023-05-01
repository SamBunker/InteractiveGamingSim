//Blackjack 
import random
import csv
# Reading/opening the CSV
def read_persons_csv(persons.csv):
    persons = []
    with open(persons.csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header row
        next(reader)
        for row in reader:
            # Create a dictionary containing the person's information
            person = {
                'first_name': row[0],
                'last_name': row[1],
                'age': int(row[2]),
                'state': row[3],
                'occupation': row[4],
                'salary': float(row[5]),
                'savings': float(row[6])
            }
            persons.append(person)
    return persons
    # Find the amount the person will bet
def get_bet_amount(person):
    # Determine the bet amount based on the person's salary and savings
    bet_percentage = (person['salary'] + person['savings']) / 100000
    bet_amount = bet_percentage * random.randint(1, 10) * 10
    return round(bet_amount)

def simulate_game(deck_count, player):
    # Determine the bet amount for this simulation run
    bet_amount = get_bet_amount(player)
    if bet_amount == 0:
        print(f"{player['first_name']} {player['last_name']} ({player['occupation']}) isn't betting anything this round.")
        return
    
def simulate_game(deck_count, min_bet, max_bet, player):
    # Set up the game
    player_hand = [draw_card() for _ in range(2)]
    dealer_hand = [draw_card(), draw_card()]
    bet_amount = random.randint(min_bet, max_bet)

    # Player's turn
    while get_hand_value(player_hand) < 21:
        # Use a simple strategy of hitting until the hand is worth 17 or more
        if get_hand_value(player_hand) < 17:
            player_hand.append(draw_card())
        else:
            break

    # Dealer's turn
    while get_hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card())

    # Determine the outcome of the game
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)
    if player_value > 21:
        return -player_bet
    elif dealer_value > 21 or player_value > dealer_value:
        return player_bet
    elif player_value == dealer_value:
        return 0
    else:
        return -player_bet

def draw_card():
    # Simulate drawing a card from a deck
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(card_values)

def get_hand_value(hand):
    # Calculate the value of a hand, accounting for aces
    value = sum(hand)
    if value > 21 and 11 in hand:
        value -= 10
    return value

# Read in the persons CSV file
persons = read_persons_csv('persons.csv')

# Run the simulation for each person
for person in persons:
    num_rounds = 10000
    results = [simulate_game(6, 10, 100, person) for _ in range(num_rounds)]
    win_ratio = sum([r > 0 for r in results]) / num_rounds
    average_payout = sum(results) / num_rounds
    print(f"{person['first_name']} {person['last_name']}: Win ratio = {win_ratio:.2f}, Average payout = ${average_payout:.2f}")