from art import logo
from replit import clear
import random

def deal_card():
  """Return a random card from deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  new_card = random.choice(cards)
  return new_card

def canpare(player_scores,dealer_scores):
  """Canpare list of cards from both and give result"""
  if player_scores==dealer_scores:
    print("Its DRAW 😑")
  elif dealer_scores==0:
    print("You lose, opponent has Blackjack 😱 ")
  elif player_scores==0:
    print("You win with a Blackjack")
  elif player_scores > 21:
    print("You went over. You lose 😭")
  elif dealer_scores > 21:
    print("oppenent went over. You win 😁")
  elif player_scores>dealer_scores:
    print("You win 😁")
  else:
    print("You lose 😭")

def calculate_score(whose_cards):
  """Take a list of cards and return the score calculated from the cards"""
  score=sum(whose_cards)
  if len(whose_cards)==2 and score==21:
    score=0
  if score>21 and 11 in whose_cards:
    whose_cards.remove(11)
    whose_cards.append(1)
  return score

def play_game():  
  player_cards=[]
  dealer_cards=[]
  is_gameover=False

  for _ in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

  while not is_gameover:
    player_scores=calculate_score(player_cards)
    dealer_scores=calculate_score(dealer_cards)
    print(f"   Your cards:{player_cards} and current scores: {player_scores}")
    print(f"   Dealer's first card: {dealer_cards[0]}")

    if player_scores==0 or dealer_scores==0 or player_scores>21:
      is_gameover=True
    else:
      player_should_deal=input("Type 'Y' to get another card, type 'N'to pass: ").lower()
      if player_should_deal=="y":
        player_cards.append(deal_card())
      else:
        is_gameover=True
  while dealer_scores!=0 and dealer_scores < 17:
    dealer_cards.append(deal_card())
    dealer_scores = calculate_score(dealer_cards)


  print(f"   Your Final Cards:{player_cards}, Final scores: {player_scores}")
  print(f"   Dealer's Final cards:{dealer_cards},Final scores: {dealer_scores}")
  canpare(player_scores, dealer_scores)
while input("Do you want to play a game of Blackjack? type 'Y'or 'N': ").lower()=="y":
  clear()
  print(logo)
  play_game()