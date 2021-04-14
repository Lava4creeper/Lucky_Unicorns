#loop the program
show_instructions = ""
while show_instructions != 'xxx':
  #ask the user if they have played before
  show_instructions = input('Have you played before?').lower()
  #If they say yes, program continues
  if show_instructions == 'yes' or show_instructions == 'y':
    print('Program Continues')
  #If they say no, output 'Display Instructions'
  elif show_instructions == 'no' or show_instructions == 'n':
    print('Display Instructions')
  #If they put in an unrecognised value, output "Error. Please input a valid value"
  else:
    print('Error. Please input a valid value.')