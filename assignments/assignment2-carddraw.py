import requests
import json

url_suffle = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url_suffle)
data_suffle = response.json()
deck_id = data_suffle["deck_id"]
url_draw = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(url_draw)
data_draw = response.json()

output_path = "./WSAA-coursework/assignments/assingment2-carddraw.json"
with open(output_path, "w") as fp:
    json.dump(data_draw, fp)

#Function to create an aray of suits in the hand
def draw_suits(data_draw):
    cards_dealt = data_draw["cards"]
    suits = []
    for card in cards_dealt:
        suit = card["suit"]
        suits.append(suit)
    return suits

#Function to create an array of ranks in the hand
def draw_rank(data_draw):
    cards_dealt = data_draw["cards"]
    ranks = []
    for card in cards_dealt:
        rank = card["value"]
        ranks.append(rank)
    return ranks

#Function to convert ranks to integer values
def convert_rank_to_value(rank):
    if rank == "ACE":
        return 14
    elif rank == "KING":
        return 13
    elif rank == "QUEEN":
        return 12
    elif rank == "JACK":
        return 11
    else:
        return int(rank)

#Function to convert integer values to ranks
def convert_value_to_rank(value):
    if value == 14:
        return "ACE"
    elif value == 13:
        return "KING"
    elif value == 12:
        return "QUEEN"
    elif value == 11:
        return "JACK"
    else:
        return str(value)

#Function to use the convert_rank_to_value function to convert all ranks in the hand to values
def ranktovalue(ranks):
    rank_values = [convert_rank_to_value(rank) for rank in ranks]
    rank_values = sorted(rank_values)
    return rank_values

#Function to use the convert_value_to_rank function to convert all values in the hand to ranks
def valuetorank(rank_values):
    ranks_raw = [convert_value_to_rank(value) for value in rank_values]
    return ranks_raw

#Function to count the number of pairs and triples in the hand
def count_pairs_triples(ranks):
    rank_counts = {}
    for rank in ranks:
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
            
    pair_count = 0
    triple_count = 0
    for rank, count in rank_counts.items():
        if count == 2:
            pair_count += 1
        if count == 3:
            triple_count += 1
    return pair_count, triple_count

#Function to check if the hand contains a four of a kind
def four(ranks):
    rank_counts = {}
    for rank in ranks:
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
    for count in rank_counts.values():
        if count >= 4:
            return True
    return False

#Function to check if the hand contains a flush
def flush(suits):
    suit_counts = {}
    for suit in suits:
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1
    
    flush = 0
    for count in suit_counts.values():
        if count >= 4:
            flush += 1
    return flush

#Function to check if the hand contains a full flush (all 5 cards of the same suit)
def full_flush(suits):
    suit_counts = {}
    for suit in suits:
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1
    
    flush = 0
    for count in suit_counts.values():
        if count == 5:
            flush += 1
    return flush

#Function to check if the hand contains a royal flush
def royal_flush(rank_values, suit):
    if set(rank_values) == {10, 11, 12, 13, 14} and full_flush(suit) == True:
        return True
    return False

#Function to check if the hand contains a straight
def straight(rank_values):
    if len(set(rank_values)) == 5 and max(rank_values) - min(rank_values) == 4:
        return True
    return False

#Function to check if the hand contains a straight flush
def straight_flush(rank_values, suit):
    if straight(rank_values) == True and full_flush(suit) == True:
        return True
    return False

#Function to check if the hand contains a full house
def full_house(pair_count, triple_count):
    if pair_count == 1 and triple_count == 1:
        return True
    return False

#Function to check if the hand contains two pairs
def two_pair(pair_count):
    if pair_count == 2:
        return True
    return False

#Main function to print the hand and the outcome of the hand in poker terms
def main():
    suits = draw_suits(data_draw)
    ranks = draw_rank(data_draw)
    pair_count, triple_count = count_pairs_triples(ranks)
    rank_values = ranktovalue(ranks)
    ranks_raw = valuetorank(rank_values)
    print("Your hand is:")
    print(f"{ranks_raw[0]} of {suits[0]}, {ranks_raw[1]} of {suits[1]}, {ranks_raw[2]} of {suits[2]}, {ranks_raw[3]} of {suits[3]}, {ranks_raw[4]} of {suits[4]}")
    
    if royal_flush(rank_values, suits) == True:
        print("Congratulation!!!!! YOU GOT A ROYAL FLUSH!!!!!!!!!")
    elif straight_flush(rank_values, suits) == True:
        print("Congratulation! You got a Straight Flush")
    elif four(rank_values) == True:
        print("Congratulation! You got a Four of a Kind")
    elif full_house(pair_count, triple_count) == True:
        print("Congratulation! You got a Full House")
    elif flush(suits) == True:
        print("Congratulation! You got a Flush")
    elif straight(rank_values) == True:
        print("Congratulation! You got a Straight")
    elif triple_count == 1:
        print("Congratulation! You got a Three of a Kind")
    elif two_pair(pair_count) == True:
        print("Congratulation! You got a Two Pairs")
    elif pair_count == 1:
        print("Congratulation! You got One Pair")
    else:
        print("You got High Card")
        
if __name__ == "__main__":
    main()