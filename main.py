import random
import time

user_score = 0
com_score = 0

def main():
  intro()
  start_game()
  score()
  outro()
  
def intro():
  welcome = ("\n!!!!!!![Welcome to Rock, Paper, Scissors]!!!!!!!!!\n")
  print(welcome)
  rule = ("Rules: Rock breaks scissors, scissors cuts paper, paper covers rock.\nIf the same two are thrown it is a tie.")
  print(rule)

def start_game():
  global user_score
  global com_score
  user_hand = input("\n[Press [r] for rock, [p] for paper, [s] for scissors]: ")
  if user_hand == "r":
    print("\n You picked rock.")
    time.sleep(2)
  elif user_hand == "p":
    print("\n You picked paper.")
    time.sleep(2)
  elif user_hand == "s":
    print("\n You picked scissors.")
    time.sleep(2)
  else:
    print("\n You didn't pick any of the choices. Try again.")
    start_game()
  
  com_hand = ["r","p","s"]
  com_hand_choice = random.choice(com_hand)
  if com_hand_choice == "r":
    print("\n The computer picked rock.")
    time.sleep(2)
  elif com_hand_choice == "p":
    print("\n The computer picked paper.")
    time.sleep(2)
  elif com_hand_choice == "s":
    print("\n The computer picked scissors.")
    time.sleep(2)
  
  if user_hand == "r":
    if com_hand_choice == "s":
      print("\n  You win! Your rock beat the computers scissors.")
      user_score = user_score+1	
      print("\n Score: [You:%s] [computer:%s]"%(user_score, com_score))
      time.sleep(2)
    elif com_hand_choice == "r":
      print("\n  its a tie.")
      time.sleep(1)
    else:
      print("\n  You lose! The computers paper beat your rock.")
      com_score = com_score+1
      print("\n Score: [You:%s] [computer:%s]"%(user_score, com_score))
      time.sleep(2)
 
  if user_hand == "p":
    if com_hand_choice == "r":
      print("\n  You win! Your paper beat the computers rock.")
      user_score = user_score+1	
      print("\n Score: [You:%s] [computer:%s]"%(user_score, com_score))
      time.sleep(2)
    elif com_hand_choice == "s":
      print("\n  You lose! The computers scissors cut your paper.")
      com_score = com_score+1
      print("\n Score: [You:%s] [computer:%s]"%(user_score, com_score))
      time.sleep(2)
    else:
      print("\n  Its a tie.")
      time.sleep(1)

  if user_hand == "s":
    if com_hand_choice == "s":
      print("\n  Its a tie.")
      time.sleep(1)
    elif com_hand_choice == "r":
      print("\n  You lose! The computers rock beat your scissors.")
      com_score = com_score+1
      print("\n Score: [You:%s] [computer:%s]"%(user_score, com_score))
      time.sleep(2)
    else:
      print("\n  You win! Your scissors cut the computers paper.")
      user_score = user_score+1	
      print("\n Score: [You:%s] [computer:%s]"%(user_score, com_score))
      time.sleep(2)

def score():
  if user_score == 3:
    print("\n   Good start!!, Your doing great!!!")
  if com_score == 3:
    print("\n   You still have a chance.")
  if user_score == 5:
    print("\n   WOW!! thats impressive.")
  if com_score == 5:
    print("\n   Come On! You can do better!")
  if user_score == 10:
    print("\n   You have achieved Legend rank!!")
  if com_score == 10:
    print("\n   This is just sad..")
  if user_score > 12:
    print("\n   I think your having too much fun.")

def outro():
  replay = input("\n[Press [t] to play again or press any other key to exit]: \n")
  if replay == "t":
    main()
  else:
    exit == "e"

main()