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

while computer_wins < 5:
    human_choice = input('Enter your choice:')
    if human_choice == 'exit':
        break
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print("Human input:",human_choice,"Computer input:",computer_choice)
    computer_wins+=int(get_winnner(human_choice,computer_choice))
    print(computer_wins)


