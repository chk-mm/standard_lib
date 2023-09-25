import random
computer_wins = 0

# human_choice = input('Enter your choice:')
def get_winnner(c1,c2):
    if c1==c2:
        return 0
    if c1 == 'rock':
        if c2 == 'paper':
            return 1
        else:
            return -1
    if c1 == 'paper':
        if c2 == 'scissors':
            return 1
        else:
            return -1
    if c1 == 'scissors':
        if c2 == 'paper':
            return -1
        else:
            return 1


while abs(computer_wins) <3:
    # human_choice = input('Enter your choice:')
    human_choice = random.choice(['rock', 'paper', 'scissors'])
    if human_choice == 'exit':
        break
    computer_choice = random.choice(['rock', 'paper', 'scissors'])


    computer_wins+=int(get_winnner(human_choice,computer_choice))
    print("Human input:",human_choice,"Computer input:",computer_choice,"Score:",computer_wins)

if computer_wins > 0 :
    print("You lose")
else:
    print("You win")


