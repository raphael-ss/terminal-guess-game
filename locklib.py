import random

def print_lockers(number_of_lockers=6, winning_locker=1):
  print("\t")
  for i in range(0, number_of_lockers):
    print("\033[1;32m###\t", end="")
  print("\n")
  for i in range(0, number_of_lockers):
    print("\033[1;32m#", end="")
    print(i+1, end="")
    print("\033[1;32m#\t", end="")
  print("\n")
  for i in range(0, number_of_lockers):
    print("\033[1;32m###\t", end="")
  print("\n")

def winning_locker(number_of_lockers=6):
  winner = random.randint(1, number_of_lockers+1)
  return winner

def select_locker(locker, number_of_lockers=6):
  if locker >= 1 and locker <= number_of_lockers:
    return locker
  else:
    print("\033[1;32mError: That locker does not exist );")
    return False


def print_trophy():
  print(""" \033[1;32m
   YEEEEEEEEEEESSSS!!! YOU WON!
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
          Thanks for playing!
  """)
  return

def print_lost():
  print(""" \033[1;32m
  NOOOOOOooo... YOU LOST!
  HERE'S CHEESE TO COMFORT YOU.

      .-"      "-.
     |""--..      '-.
     |      ""--..   '-.
     |.-. .-".    ""--..".
     |'./  -_'  .-.      |
     |      .-. '.-'   .-'
     '--..  '.'    .-  -.
          ""--..   '_'   :
                ""--..   |
                      ""-' 
  """)
  return


def guess(guess_number, winning_locker=1):
  if guess_number == winning_locker:
    print_trophy()
  else:
    print_lost()
  return

def play(option=1):
  if option == 1:
    print_lockers()
    print("\033[1;32mGuess... the... LOCKER!!!")
    guess_number = int(input("\033[1;0mYour guess: "))
    guess_number = select_locker(guess_number)
    if guess_number == False:
      return False
    winner = winning_locker()
    guess(guess_number, winner)
    return True
  elif option == -1:
    print(""" \033[1;32m
    
    This is a guessing game. By default, we have 6 lockers. 
    Choose the right one to win the game. 
    Everytime you play, the winning locker will change.
    Just type in your guess and let the
    destiny (or the computer) tell you!

    This game was made by soaressuarez
    
    """)
    return True
  elif option == 0:
    return False
  else:
    print("\033[1;32mChoose a valid option!")
    return True