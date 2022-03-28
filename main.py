# Account for user guess being in wordList: Done 
# If not=, subtract a guess for loop and continue..?: Done
# Print in one line: Done
# Last Step: Adding a word list using a package.: Done



from nltk.corpus import words
import random
from termcolor import colored


wordList = []
for i in words.words():
  if len(i) == 5:
    wordList.append(i.upper())
    
wordChoice = [i for i in random.choice(wordList).upper()]
print(wordChoice)
guess = 0 

print("Here are the rules: \nGreen Letters means they're in the correct position\nYellow Letters are in the word...but in the wrong position\nWhite Letters are not in the word\nEmpty Guesses and Words not equal to 5 letters are not counted as guesses.\n")





while guess <= 6:
  guess += 1
  userInput = input('Input Word Guess: ').upper()
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
      
      
  print(''.join(emptyList))



      
      