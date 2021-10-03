import random
from hangman_guessing import guess_list
from hangman_life import game_name, lives

'''Imported all the necessary libraries including random, hangman lists which contain lists of words that are going to be used in the game.
Also it includes the design of the game name Hangman and the design of the live count

'''
guessing_word = random.choice(guess_list).lower()                   # got a number out from the list of the words through random function.

lives_index= 0                                                      # the index that tells which design of live has to be printed

blank_index=-1                                                      #index for the word that is getting updated by user's choice of words

length_of_word=len(guessing_word)                                   #length of the word that has been randomly selected

real_word=guessing_word                                             #a dummy word to finally print out in case the word gets changed

blank_word=length_of_word * ["_"]                                   # blank_word is an output that will be printed everytime. making a list according to the length of the word chosen for blank_word

print(game_name)                                                    #game name design Hangman will be printed

'''Entering the while loop'''
while lives_index<7 and ("_" in blank_word):                        # loop to check if the word has been guessed or the lives are lost (Basically checking if the game's over or not)
    
    print(f"{' '.join(blank_word)}")                                # print the word so far guessed by the user
    
    guess=input(("Enter your guess:"+ guessing_word))               #take input from the user

    for i in range(length_of_word):                                 #iterating till the length of the Guessing_word is reached
        
        if guessing_word[i]==guess:                                 #condition to see if the letter guessed by the user matches the 
            
            blank_index=i                                           #assigning the blank word's(updating word) index to assign the character
            guessing_word=guessing_word[:i]+"_"+guessing_word[i+1:] #changing the guessed letter to "_" to avoid it from getting repeated
            # print(guessing_word) FOR TESTING PURPOSES
            
            print(f"The letter you guessed is {guess} and it is in the word")
            blank_word[blank_index]=guess    

    if(blank_index==-1):                                            #if blank was not changed, it remained -1 which means the letter was not in the word
        print(f"The letter you guessed is {guess} which is not in the word") #printing conclusion message
        lives_index+=1                                              #incrementing the life index if you didn't guess it right

    
    if lives_index<7:
        print(lives[lives_index])                                   #printing life status
    blank_index=-1

''' Out from the while loop  to print the actual result'''

if lives_index==7:
    print("Sorry you lost....Better luck next time. The word was "+ real_word)
else: 
    print(f"Whooohoooo...Congrats, You have won the game. Excellent guessing. The word was {' '.join(blank_word)}")

