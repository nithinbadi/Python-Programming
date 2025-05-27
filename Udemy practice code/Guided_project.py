'''
War card game 

Rules:
1. Cards are split in perfect half
2. Each round a card is picked and the card that has the highest rarity wins and the two cards go to the winner.
3. If the cards have the same rarity, then they go to war.
4. Each player takes out a set of cards and set aside and pull out a new card from each.
5. Repeat until one Player has no cards and the other player wins.



To construct this game, we will create:
1. Card Class
2. Deck Class
3. Player Class
4. Game Logic

'''

import random

# Suits
suits = ['Spades','Hearts','Diamonds','Clubs']

# Numbers
numCards = {
    "Ace":1,
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5,
    "Six":6,
    "Seven":7,
    "Eight":8,
    "Nine":9,
    "Ten":10,
    "Jack":11,
    "Queen":12,
    "King":13
}


class Card():

    def __init__(self,num,suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        return f'{self.num} of {self.suit}'



class Deck():
    
    def __init__(self):
        self.deck = []

        for suit in suits:
            for i in numCards:
                self.deck.append(Card(i,suit))
    
    def split_deck(self):
        mid = len(self.deck)//2
        return self.deck[:mid],self.deck[mid:]

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return self.deck


    def __str__(self):
        for card in self.deck:
            print(card)
        return ""
    def __len__(self):
        return len(self.deck)
    



class Player():
    

    def __init__(self,cards):
        self.cards = cards
        pass

    def add(self,card):
        self.cards.insert(0,card)
        

    def remove(self):
        return self.cards.pop()


def check_winner(player1_choice,player2_choice):
    # Order high to low -> ['Spades','Hearts','Diamonds','Clubs']
    if suits.index(player1_choice.suit) < suits.index(player2_choice.suit):
        return "Player 1"
    elif suits.index(player1_choice.suit) > suits.index(player2_choice.suit):
        return "Player 2" 
    else:
        # Numbers priority "King" to "Ace"
        if numCards[player1_choice.num] > numCards[player2_choice.num]:
            return "Player 1"
        elif numCards[player1_choice.num] < numCards[player2_choice.num]:
            return "Player 2"
        else:
            # No winner meaning it's tie and the players go to war
            return ""
        


deck = Deck()
deck.shuffle_deck()
player1_deck, player2_deck = deck.split_deck()

# BEGIN THE GAME
player1 = Player(player1_deck)
player2 = Player(player2_deck)


# GAME LOOP
while True:
   
    
    
    
    if len(player1.cards) == 0 or len(player2.cards) == 0:
        break
    player1_choice = player1.remove()
    player2_choice = player2.remove()


    print(player1_choice)
    print(player2_choice)
    
    
    
    # We go to war
    if check_winner(player1_choice,player2_choice) == "Player 1":
        
        # Adds both cards to Player 1's deck
        player1.add(player2_choice)
        player1.add(player1_choice)
    elif check_winner(player1_choice,player2_choice) == "Player 2":
        
        # Adds both cards to Player 2's deck
        player2.add(player1_choice)
        player2.add(player2_choice)

    else:
        player1_choices = []
        player2_choices = []
        # We go to war
        
        while True:
            print("1")
            player1_top3 = player1.cards[:3]
            player2_top3 = player2.cards[:3]
            
            for i in range(3):
                
                if check_winner(player1_top3[i],player2_top3[i]) == "Player 1":
                    i1 = True
                    i2=False
                elif check_winner(player1_top3[i],player2_top3[i]) == "Player 2":
                    i1=False
                    i2 = True
                else:
                    i1 = False
                    i2 = False
            if i1:
                for k in range(3):
                    player1.add(player1_top3[k])
                    player1.add(player2_top3[k])
                break
            elif i2:
                for k in range(3):
                    player2.add(player1_top3[k])
                    player2.add(player2_top3[k])
                break
            else:
                for k in range(3):
                    player1.add(player1_top3[k])
                    player2.add(player2_top3[k])
                player1_deck.shuffle()
                player2_deck.shuffle()
                
            
    print(len(player1.cards))
    print(len(player2.cards))


if len(player2.cards) == 0:
    print("Player 1 wins")
elif len(player1.cards) == 0:
    print("Player 2 wins")

    




# d = Deck()
# c= Card(1,suits[1])
# d.shuffle_deck()
# first_half,second_half = d.split_deck()


# for card in first_half:
#     print(card)
# print(len(d))

# for card in second_half:
#     print(card)

# print(len(first_half))
# print(len(second_half))