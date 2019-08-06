import random


def rps():
    while True:
        choice = input('Make your choice: ')
        choice = choice.lower()
        print("My choice is: {}".format(choice))
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        # computer_choice = choices[random.randint(0, len(choices) - 1)]
        print("The computer choice is: {}".format(computer_choice))
        if choice in choices:
            if choice == computer_choice:
                print('The match is tied.')
            if choice == choices[0]:
                if computer_choice == choices[1]:
                    print('You lose, sorry.')
                elif computer_choice == choices[2]:
                    print('You win!')
            if choice == choices[1]:
                if computer_choice == choices[2]:
                    print('You lose, sorry.')
                elif computer_choice == choices[0]:
                    print('You win!')
            if choice == choices[2]:
                if computer_choice == choices[0]:
                    print('You lose, sorry.')
                elif computer_choice == choices[1]:
                    print('You win!')
        else:
            print('You have entered an incorrect choice.')
            break
        print('\n')


rps()
