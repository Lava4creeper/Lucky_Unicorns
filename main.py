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
  #If they say no, output 'Display Instructions'
  elif response == 'no' or response == 'n':
    response = 'no'
    print('You answered ' + response)
    print('Display Instructions')
  #If they put in an unrecognised value, output "Error. Please input a valid value"
  else:
    print('Error. Please input a valid value.')