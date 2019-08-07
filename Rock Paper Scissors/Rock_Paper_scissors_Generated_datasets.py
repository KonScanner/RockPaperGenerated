import random
import matplotlib.pyplot as plt
import numpy as np
import os
import time
from threading import Thread

""" Initializing time taken to complete process"""
start = time.time()

""" Initializing lists & number of runs"""
data = []
threads = []
c = ['rock', 'paper', 'scissors']
n = 10000  # Total number of runs

""" Fetches current directory"""
current_directory = os.getcwd()

""" Fetches path to data, such for later use"""
path_to_data = current_directory + '/data/Randomized/'


def calculation():
    """ Rock paper scissors function. With the extra
    generated data per run"""
    i = 0
    for x in range(len(c)):
        a = random.randint(1, 100000)
        random.seed(a)
        print(a)
        while i <= n:
            choice = c[x]
            choice = choice.lower()
            choices = ['rock', 'paper', 'scissors']
            computer_choice = choices[random.randint(0, len(choices) - 1)]
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
            i += 1
            data.append(result_index)
        np.savetxt(path_to_data + str(object=n) +
                   "_" + str(object=c[x]) + "_data.csv", data, delimiter=",")


def plot_dataset():
    """ Function that loads up the dataset and plots
    histograms on the randomized saved sets for n number of runs"""

    dataset0 = np.genfromtxt(path_to_data + str(object=n) +
                             "_" + str(object=c[0]) + "_data.csv", delimiter=', ')
    dataset1 = np.genfromtxt(path_to_data + str(object=n) +
                             "_" + str(object=c[1]) + "_data.csv", delimiter=', ')
    dataset2 = np.genfromtxt(path_to_data + str(object=n) +
                             "_" + str(object=c[2]) + "_data.csv", delimiter=', ')
    dataset = [dataset0, dataset1, dataset2]

    for x in range(len(c)):
        loc = (0.25, 1.25, 2.25)
        bins = [0, 0.5, 1, 1.5, 2, 2.5]
        weights = np.ones_like(dataset[x]) / float(len(dataset[x]))
        plt.figure(str(c[x]) + ' dataset')
        plt.grid('both')
        plt.hist(dataset[x], bins=bins, density=False, weights=weights, rwidth=0.75,
                 label='Rock Paper Scissors: {} number of runs, player choice = {}'.format(n, c[x]))
        plt.xlabel('Events that could occur')
        plt.ylabel(r'$\rho_{{event \ occuring}}$')
        plt.title(
            'Events that could occur and density of occurance, {}'.format(c[x]))
        plt.xticks(loc, ('Tie', 'Win', 'Lose'))
    plt.show()


def Threading_Process():
    """ Threading and mapping function"""
    for i in range(os.cpu_count()):
        print('registering thread {}'.format(i))
        threads.append(Thread(target=calculation))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


Threading_Process()

end = time.time()
print(f'The final time taken to do calculation was {end-start} s')
plot_dataset()
