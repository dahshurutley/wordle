# Output letters that arent in word within list 

from nltk.corpus import words
import random
from termcolor import colored

wordList = []
wordsVoid = set()
for i in words.words():
  if len(i) == 5:
    wordList.append(i.upper())
wordChoice = [i for i in random.choice(wordList).upper()]
guess = 0 

print("Here are the rules: \nGreen Letters means they're in the correct position\nYellow Letters are in the word...but in the wrong position\nWhite Letters are not in the word\nEmpty Guesses and Words not equal to 5 letters are not counted as guesses.\n")

while guess <= 6:
  guess += 1
  userInput = input('Input Word Guess: ').upper()
  userContent = [i for i in userInput]
  emptyList = []

  if userContent == wordChoice:
    print(colored(f"{''.join(userContent)}", 'green'))
    print(f'Correct, the word was {"".join(wordChoice)}. It took you {guess} Tries.')
    break
  if userInput in wordList:
    for i in range(0, len(wordChoice)):
      if userContent[i] in wordChoice: 
        if userContent[i] == wordChoice[i]:
          emptyList.append(colored(f'{userContent[i]}', 'green'))
        else: 
          emptyList.append(colored(f'{userContent[i]}', 'yellow'))
      else:
        emptyList.append(colored(f'{userContent[i]}', 'white'))
        wordsVoid.add(userContent[i])
  else: 
    if len(userContent) != 5: 
      print('Not a Five Letter Word\n')
      guess -= 1
      continue
    if userInput not in wordList:
      print('Not in Word List\n')
      guess -= 1
      continue
  print(''.join(emptyList))
  print(f'Letters not in word: {sorted(wordsVoid)}\n') 

print(f'The Word Was {"".join(wordChoice).lower().capitalize()}') 



      
      