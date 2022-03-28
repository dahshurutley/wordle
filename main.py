# Account for user guess being in wordList: Done 
# If not=, subtract a guess for loop and continue..?: Done
# Print in one line: Done
# Last Step: Adding a word list using a package. 

import random
from termcolor import colored
wordList = ['CAULK', 'HAPPY', 'PAPPY']
wordChoice = [i for i in random.choice(wordList)]
print(wordChoice)
guess = 0 

while guess <= 6:
  guess += 1
  userInput = input('Input Word Guess')
  userContent = [i for i in userInput]
  print(userContent)
  emptyList = []

  if userContent == wordChoice:
    print(colored(f"{''.join(userContent)}", 'green'))
    print(f'Correct, the word was {"".join(wordChoice)}. It took you {guess} Tries.')
    break

  if userInput in wordList:
    for i in range(0, len(wordChoice)):
      if userContent[i] in wordChoice: 
        if userContent[i] == wordChoice[i]:
          # Return Joined string of letters
          emptyList.append(colored(f'{userContent[i]}', 'green'))
        else: 
          emptyList.append(colored(f'{userContent[i]}', 'yellow'))
      else:
        emptyList.append(colored(f'{userContent[i]}', 'white'))
  else: 
    if len(userContent) != 5: 
      print('Not a Five Letter Word')
      guess -= 1
      continue

    if userInput not in wordList:
      print('Not in Word List')
      guess -= 1
      continue 
      
  print(''.join(emptyList))


      
      