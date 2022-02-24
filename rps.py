import random

wins = 0
losses = 0

def bothChoices(choice, userGuess):
    print(f'Your choice: {userGuess}')
    print(f'Computer choice: {choice}')

def gameplay():
    choice = random.choice(['rock', 'paper', 'scissors'])
    userGuess = input('Choose rock, paper, or scissors: ')
    print()
    global wins
    global losses
    #prints if you won, lost, or had a draw and also returns number to calculate total score
    if userGuess == 'rock':
        if choice == 'rock':
            bothChoices(choice, userGuess)
            print('Draw!')
        elif choice == 'paper':
            bothChoices(choice, userGuess)
            print('You lost!')
            losses += 1
        else:
            bothChoices(choice, userGuess)
            print('You won!')
            wins += 1
    elif userGuess == 'paper':
        if choice == 'rock':
            bothChoices(choice, userGuess)
            print('You won!')
            wins += 1
        elif choice == 'paper':
            bothChoices(choice, userGuess)
            print('Draw!')
        else:
            bothChoices(choice, userGuess)
            print('You lost!')
            losses += 1
    elif userGuess == 'scissors':
        if choice == 'rock':
            bothChoices(choice, userGuess)
            print('You lost!')
            losses += 1
        elif choice == 'paper':
            bothChoices(choice, userGuess)
            print('You won!')
            wins += 1
        else:
            bothChoices(choice, userGuess)
            print('Draw!')
    else:
        print('Invalid input.')

#gameplay loop
games = int(input('How many games would you like to play?: '))
for i in range(games):
    gameplay()
    print(f'You have {wins} wins.')
    print(f'You have {losses} losses.')
    print()

#end result
if wins > losses:
    print('You won the match!')
elif wins < losses:
    print('You lost the match!')
else:
    print('You tied the match!')
