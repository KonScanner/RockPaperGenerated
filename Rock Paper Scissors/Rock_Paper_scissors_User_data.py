import random
import matplotlib.pyplot as plt
import numpy as np
import os
import time

start = time.time()
data = []
threads = []
n = 10

current_directory = os.getcwd()
path_to_data = current_directory + '/data/User_Based'


def calculation_from_game():
    i = 0
    while i <= n:
        # choice = input('Make your choice: ')
        choice = input('Make a choice: ')
        choice = choice.lower()
        choices = ['rock', 'paper', 'scissors']
        # computer_choice = random.choice(choices)
        computer_choice = choices[random.randint(0, len(choices) - 1)]
        # print("The computer choice is: {}".format(computer_choice))
        choice_dict = {'rock': 0, 'paper': 1, 'scissors': 2}
        choice_index = choice_dict.get(choice, 3)
        computer_index = choice_dict.get(computer_choice)

        result_matrix = [[0, 2, 1],
                         [1, 0, 2],
                         [2, 1, 0],
                         [3, 3, 3]]
        # 0 is a tie
        # 1 is a win
        # 2 is a loss
        result_index = result_matrix[choice_index][computer_index]
        result_messages = ['it is a tie.', 'You win!',
                           'You lost.', 'Invalid choice, try again.!']
        result = result_messages[result_index]
        # print(result)
        i += 1
        data.append(result_index)
    np.savetxt(path_to_data + '\ ' + str(object=n) +
               "_" + 'UserInput' + "_data.csv", data, delimiter=",")


def plot_dataset():
    dataset = np.genfromtxt(path_to_data + '\ ' + str(object=n) +
                            "_" + 'UserInput' + "_data.csv", delimiter=', ')
    loc = (0.25, 1.25, 2.25, 3.25)
    bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]
    weights = np.ones_like(dataset) / float(len(dataset))
    plt.figure('User input dataset for {} number of tries'.format(n))
    plt.grid('both')
    plt.hist(dataset, bins=bins, density=False, weights=weights, rwidth=0.75,
             label='Rock Paper Scissors: {} number of runs, User input!'.format(n))
    plt.xlabel('Events that could occur')
    plt.ylabel(r'$\rho_{{event \ occuring}}$')
    plt.title(
        'Events that could occur and density of occurance, User input')
    plt.xticks(loc, ('Tie', 'Win', 'Lose', 'Invalid Input'))
    plt.show()


calculation_from_game()
plot_dataset()
end = time.time()

print(f'The final time taken to do calculation was {end-start} s')
