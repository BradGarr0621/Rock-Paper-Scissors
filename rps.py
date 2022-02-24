import random

wins = 0

def bothChoices(choice, userGuess):
    print(f'Your choice: {userGuess}')
    print(f'Computer choice: {choice}')

def gameplay():
    choice = random.choice(['rock', 'paper', 'scissors'])
    userGuess = input('Choose rock, paper, or scissors: ')
    print()
    global wins
    #prints if you won, lost, or had a draw and also returns number to calculate total score
    if userGuess == 'rock':
        if choice == 'rock':
            bothChoices(choice, userGuess)
            print('Draw!')
            wins = wins
        elif choice == 'paper':
            bothChoices(choice, userGuess)
            print('You lost!')
            wins = wins - 1
        else:
            bothChoices(choice, userGuess)
            print('You won!')
            wins = wins + 1
    elif userGuess == 'paper':
        if choice == 'rock':
            bothChoices(choice, userGuess)
            print('You won!')
            wins = wins + 1
        elif choice == 'paper':
            bothChoices(choice, userGuess)
            print('Draw!')
            wins = wins
        else:
            bothChoices(choice, userGuess)
            print('You lost!')
            wins = wins - 1
    elif userGuess == 'scissors':
        if choice == 'rock':
            bothChoices(choice, userGuess)
            print('You lost!')
            wins = wins - 1
        elif choice == 'paper':
            bothChoices(choice, userGuess)
            print('You won!')
            wins = wins + 1
        else:
            bothChoices(choice, userGuess)
            print('Draw!')
            wins = wins
    else:
        print('Invalid input.')

#gameplay loop
games = int(input('How many games would you like to play?: '))
for i in range(games):
    gameplay()
    print('You have ' + str(wins) + ' wins.')
    print()

#end result
if wins > 0:
    print('You won the match!')
elif wins < 0:
    print('You lost the match!')
else:
    print('You tied the match!')
