#defining instructions
def yes_no_response():
  #loop the program
  response = ""
  while response != 'xxx':
    #ask the user if they have played before
    response = input('Have you played before?').lower()
    #If they say yes, program continues
    if response == 'yes' or response == 'y':
      response = 'yes'
      print('You answered ' + response)
      print('Program Continues')
    #If they say no, Display Instructions
    elif response == 'no' or response == 'n':
      response = 'no'
      print('You answered ' + response)
      instructions()
    #If they put in an unrecognised value, output "Error. Please input a valid value"
    else:
      print('Error. Please input a valid value.')
def instructions():
  print('**** HOW TO PLAY ****')
  print()
  print('The rules of the game go here')
  print()
  return ""
yes_no_response()