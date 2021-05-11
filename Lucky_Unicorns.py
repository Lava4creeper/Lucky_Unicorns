#Lucky Unicorns Full Version 1 was developed by Thomas Gardner on 9/5/2021
#Checking if the user has played before
def yes_no_response():
  #creating exit code
  Played_Before = ""
  while Played_Before != 'xxx':
    #ask the user if they have played before
    Played_Before = input('Have you played before? ').lower()
    #If they say yes, program continues
    if Played_Before == 'yes' or Played_Before == 'y':
      Played_Before = 'Yes'
      print('You answered ' + Played_Before)
      print('Program Continues')
      #Program continuing
      number_checker('How much money are you playing with today? $', 0, 100, 0)
    #If they say no, Instructions are displayed
    elif Played_Before == 'no' or Played_Before == 'n':
      Played_Before = 'No'
      print('You answered ' + Played_Before)
      print('Showing Instructions')
      #Instructions
      print()
      print('**** HOW TO PLAY ****')
      print()
      print('The rules are simple. You will choose ')
      print('an amount of money to play with between')
      print('$1 and $10, and then be given the option to')
      print('Generate a token. The token will either be a ')
      print('Donkey and you will lose $1, a Horse or Zebra')
      print('and you will lose 50c, or a unicorn where you')
      print('will win $4.')
      print()
      print("Program Continues")
      #Program continuing
      number_checker('How much money are you playing with today? $', 0, 100, 0)
    #If they put in an unrecognised value, output an error
    else:
      print('Error. "{}" is not a valid input. Please input "Yes" or "No".'.format(Played_Before))
#Asking the user how much money they will play with
def number_checker(question, low, high, how_much):
  error = 'Please enter a whole number between 1 and 10'
  while how_much != 'xxx':
    try:
      #ask how much money they are paying with
      how_much = int(input(question))
      #If the number is between 1 and 10, accept it
      if low < how_much <= high:
        print('You payed ${}'.format(how_much))
        game_body(how_much)
      #If the number is below 1 or above 10 ask again
      else:
        print(error)
    #If the input isn't an integer ask again
    except ValueError:
      print(error)
#Playing the game
def game_body(how_much):
  import random
  #setting rounds to zero
  rounds_played = 0
  #Starting the game
  play_again = input("Press <Enter> to play... ").lower()
  #looping the game
  while play_again != "xxx":
    #increase # of rounds played
    rounds_played += 1
    #Print round number
    print()
    print('*** Round #{} ***'.format(rounds_played))
    #selecting token randomly
    chosen_num = random.randint(1, 100)
    #setting a 5% chance for a Unicorn and altering the players balance
    if 1 <= chosen_num <= 5:
      chosen = 'Unicorn'
      how_much += 4
      #Informing the player of their balance and token
      print('Token: {}, Balance: ${:.2f}'.format(chosen, how_much))
    #Setting a 30% chance for a Donkey and altering the players balance
    elif 6<= chosen_num <= 36:
      chosen = 'Donkey'
      how_much -= 1
      #Informing the player of their balance and token
      print('Token: {}, Balance: ${:.2f}'.format(chosen, how_much))
    #Setting a 65% chance for a Horse or Zebra
    else:
      #Deciding between a Horse or Zebra
      if chosen_num % 2 ==0:
        chosen = 'Horse'
      else:
        chosen = 'Zebra'
      #Altering the players balance
      how_much -= 0.5
      #Informing the player of their balance and token
      print('Token: {}, Balance: ${:.2f}'.format(chosen, how_much))
    #If the player runs out of money, stop the game
    if how_much < 1:
      print('Sorry, you have run out of money. Thank you for playing Lucky Unicorns! Have a great day.')
      print()
      #Go back to the start
      yes_no_response()
    #If the player still has money, continue the game
    else:
      play_again = input("Press Enter to play again " "or 'XXX' to quit").lower()
  print('Thanks for playing Lucky Unicorns! Your final balance was ${}. Have a great day!'.format(how_much))
  print()
  #Go back to the start
  yes_no_response()
#Start the program
yes_no_response()
