################################################################################
#
#  Coursera: An Introduction to Interactive Programming in Python (Part 2)
#  Mini-project #6 - Blackjack
#  This program use simplegui (http://www.codeskulptor.org)
#
#  The game logic for our simplified version of Blackjack is as follows.
#  The player and the dealer are each dealt two cards initially with one of the
#  dealer's cards being dealt faced down (his hole card). The player may then ask
#  for the dealer to repeatedly "hit" his hand by dealing him another card. If,
#  at any point, the value of the player's hand exceeds 21, the player is
#  "busted" and loses immediately. At any point prior to busting, the player may
#  "stand" and the dealer will then hit his hand until the value of his hand
#  is 17 or more. (For the dealer, aces count as 11 unless it causes the
#  dealer's hand to bust). If the dealer busts, the player wins. Otherwise,
#  the player and dealer then compare the values of their hands and the hand
#  with the higher value wins. The dealer wins ties in our version.
#
################################################################################

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc,
                          CARD_SIZE,
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)


# define hand class
class Hand:
    def __init__(self):
        self.collection = []

    def __str__(self):
        result = "Hand contains"
        for item in self.collection:
            result += " " + str(item)
        return result

    def add_card(self, card):
        self.collection.append(card)

    def get_value(self):
        hand_value = 0
        aces_in_hand = False
        for item in self.collection:
            if item.get_rank() == "A":
                aces_in_hand = True
            hand_value += VALUES.get(item.get_rank())
        if aces_in_hand is False:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value

    def draw(self, canvas, pos):
        for index_card in self.collection:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(index_card.rank),
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(index_card.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE,
                              [pos[0] + CARD_CENTER[0] + 73 * self.collection.index(index_card),
                               pos[1] + CARD_CENTER[1]],
                              CARD_SIZE)


# define deck class
class Deck:
    def __init__(self):
        self.deck = [Card(dummy_suits, dummy_ranks) for dummy_suits in SUITS for dummy_ranks in RANKS]

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    def __str__(self):
        result = "Deck contains"
        for item in self.deck:
            result += " " + str(item)
        return result


# define event handlers for buttons
def deal():
    global outcome, in_play, global_deck, player, dealer, score
    if in_play:
        score -= 1
    global_deck = Deck()
    global_deck.shuffle()
    player = Hand()
    player.add_card(global_deck.deal_card())
    player.add_card(global_deck.deal_card())
    dealer = Hand()
    dealer.add_card(global_deck.deal_card())
    dealer.add_card(global_deck.deal_card())
    outcome = ""
    in_play = True


def hit():
    global in_play, player, score, outcome
    if in_play:
        player.add_card(global_deck.deal_card())
        if player.get_value() > 21:
            score -= 1
            outcome = "You have busted"
            in_play = False


def stand():
    global in_play, player, dealer, score, outcome
    if in_play:
        while dealer.get_value() <= 17:
            dealer.add_card(global_deck.deal_card())
        if 21 >= dealer.get_value() >= player.get_value():
            score -= 1
            outcome = "Dealer win"
        else:
            score += 1
            outcome = "Player win"
        in_play = False
        print "Player: " + str(player.get_value()) + "/Dealer: " + str(dealer.get_value())


# draw handler
def draw(canvas):
    dealer.draw(canvas, [50, 200])
    player.draw(canvas, [50, 400])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                          [50 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]],
                          CARD_SIZE)
        canvas.draw_text("hit or stand?", [260, 380], 20, "White")
    else:
        canvas.draw_text("New deal?", [260, 380], 20, "White")
    canvas.draw_text(outcome, [260, 340], 30, "White")
    canvas.draw_text("Dealer", [50, 170], 20, "White")
    canvas.draw_text("Player (" + str(player.get_value()) + ")", [50, 380], 20, "White")
    canvas.draw_text("Score: " + str(score), [260, 100], 25, "White")
    canvas.draw_text("BlackJack", [205, 50], 45, "White")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
