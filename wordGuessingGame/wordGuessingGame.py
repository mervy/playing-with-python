# Jogo da advinhação de palavras
# https://acervolima.com/programa-python-para-jogo-de-adivinhacao-de-palavras/

import random

name = input("What is your name? ")

print ("Good luck! ", name)

words = ['abacaxi', 'abacate', 'amora', 'ameixa', 'banana', 'bacuri', 'buriti', 'caju', 'carambola', 'cacau', 'damasco', 'durião', 'embaúba', 'figo','framboesa', 'goiaba', 'graviola', 'groselha', 'heisteria', 'ingá', 'jambo', 'jabuticaba', 'kiwi', 'laranja', 'limão', 'lichia', 'mamão', 'melancia', 'marmelo', 'melão', 'nectarina', 'nêspera', 'olho-de-boi', 'pera', 'pêssego', 'physalis', 'quina', 'romã', 'seriguela', 'sapoti', 'tâmara', 'tamarindo','tangerina', 'umbu', 'uva', 'veludo', 'wampee', 'xixá', 'yamamomo', 'zimbro']

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0: 
    failed = 0
    
    for char in word:
        if char in guesses:
            print (char)
        else:
            print("_")
            failed += 1
                    
    if failed == 0:
        print ("You Win")
        print("The word is: ", word)
        break
    
    guess = input("guess a character:")
    
    guesses += guess
    
    if guess not in word:
        turns -= 1
        
        print("Wrong")
        
        print("You have", + turns, 'more guesses')
        
        if turns == 0:
            print("You loose")
        