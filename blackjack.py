# Virtual Blackjack Game
# Created as a project for The Complete Python Bootcamp by Jose Portilla 

import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
        print('')

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except:
            print('Sorry. You must input a whole number.')
        else:
            if chips.bet > chips.total:
                print('Sorry. You do not have enough chips to bet this amount.')
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing 
    
    while True:
        choice = input('Would you like to hit or stand?')
        if choice.lower() == 'hit':
            hit(deck,hand)
        elif choice.lower() == 'stand':
            playing = False
        else:
            print('Sorry, please choose again.')
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print('Player busts!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('Player wins!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Dealer busts!')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('Dealer wins!')
    chips.lose_bet()

def push(player, dealer):
    print("Tie game! It's a push!")

while True:

    print("Let's play Blackjack!")

    deck = Deck()
    deck.shuffle()

    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    chips = Chips()

    take_bet(chips)

    show_some(player,dealer)

    while playing:
        hit_or_stand(deck,player)
        show_some(player,dealer)

        if player.value > 21:
            player_busts(player,dealer,chips)
            break 

        if player.value <= 21:
            while dealer.value < 17:
                print(f'in while loop...{dealer.value}')
                hit(deck,dealer)
                print(f'in while loop...{dealer.value}')

            show_all(player,dealer)

            if dealer.value > 21:
                dealer_busts(player, dealer, chips)
                break

            elif dealer.value > player.value:
                dealer_wins(player,dealer,chips)
                break

            elif dealer.value == player.value:
                push(player,dealer)
                break


    print(f'Player has {player.value} points')
    print(f'Player has {chips.total} chips.')

    play_again = input('Would you like to play again?')

    if play_again[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break


            

            













        


