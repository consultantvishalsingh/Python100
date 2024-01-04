
print("Jai Durga Mata")

import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_List= ['ram','shyam','maa']
selected_word= random.choice(word_List)

# Print Logo Of the Game
print(logo)

#Loop and print _ blank-spaces instead of word
length=len(selected_word)
Fill=[]
for i in range(length):
    Fill+="_"
print("\n\nSPACES TO FILL\n\n",Fill)

#Fill the blank space with the guess word
end= False
live= 6
while not end:
    user_guess=input("\nEnter a letter ").lower()
    if user_guess in Fill:
        print("You have already guessed",user_guess)
    for i in range(length):
        letter = selected_word[i]
        if letter == user_guess:
            Fill[i]=letter   
    print(Fill)
    if "_" not in Fill:
        end=True
        print("You Win")
    if user_guess not in selected_word:
        live-=1
        print(stages[live])
        print(Fill)
        if live==0:
            end=True
            print("Game Over\n")

# Check if a List contain a particular element
""" The in keyword has two purposes:
The in keyword is used to check if a value is present in a sequence (list, range, string etc.).
The in keyword is also used to iterate through a sequence in a for loop: """



