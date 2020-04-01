import random

money  = 100

#Write your game of chance functions here
num = random.randint(1, 2)

def coin_flip(guess,bet):
  win = random.randint(1,2)
  
  if money < bet:
    print("You don't have enough money to bet.")
    return 0 
  elif bet <= 0:
    print ("Please enter a positive bet.")
    return 0 
  
  if (guess == "Heads" and win == 1) or (guess == "Tails" and win == 2):
    print ("The user has won " + str(bet) + " dollars.")
    return bet 
  else:
    print ("The user has lost " + str(-bet) + " dollars.")
    return -bet
  
#heads being 1 and tails being 2

def cho_han (guess,bet):
  if money < bet:
    print("You don't have enough money to bet.")
    return 0 
  elif bet <= 0:
    print ("Please enter a positive bet.")
    return 0 

  dice_sum = random.randint(1,6) + random.randint(1,6)
  
  if dice_sum % 2 == 0 and guess == "Even":
    print ("You have won " + str(bet) + " dollars.")
    return bet 
  elif dice_sum % 2 == 1 and guess == "Odd":
    print ("You have won " + str(bet) +  " dollars.")
    return bet 
  else:
    print ("You have lost " + str(bet) + " dollars.")
    return -bet
  
#even being 1 and odd being 2

def card_picking (bet):
  if money < bet:
    print("You don't have enough money to bet.")
    return 0 
  elif bet <= 0:
    print ("Please enter a positive bet.")
    return 0 
  
  player1 = random.randint(1,10)
  player2 = random.randint(1,10)
  
  if player1 > player2:
    print ("Player 1 has won " + str(bet) + " dollars and player 2 has lost " + str(-bet) + " dollars.")
    return bet 
  
  elif player1 < player2:
    print ("Player 2 has won " + str(bet) + " dollars and player 1 has lost " + str(-bet) + " dollars.")
    return -bet 
  
  else:
    print ("The game is a draw.")
    return 0 

#player 1 is the player playing the games in card_picking function

def roulette(guess,bet):
  if money < bet:
    print("You don't have enough money to bet.")
    return 0 
  
  elif bet <= 0:
    print ("Please enter a positive bet.")
    return 0 
  
  win = random.randint(0,37)
  
  if guess == win:
    print ("You have won " + str(bet*35) + " dollars.")
    return bet*35
  elif guess == "Even" and win % 2 == 0 and win!=0:
    print("You have won " + str(bet) + " dollars.")
    return bet
  elif guess == "Odd" and win % 2 == 1 and win!=37:
    print("You have won " + str(bet) + " dollars.")
    return bet
  elif guess == "Even" and win % 2 != 0:
    print("You have lost " + str(bet) + " dollars.")
    return -bet 
  elif guess == "Odd" and win % 2 != 0:
    print("You have lost " + str(bet) + " dollars.")
    return -bet
  else:
    print("You have lost " + str(bet) + " dollars.")
    return -bet
#Call your game of chance functions here

money += coin_flip("Heads",10)

money += cho_han("Even",10)

money += card_picking(10)

money += roulette("Odd",10)

print("You currently have " + str(money) + " dollars.")
                  