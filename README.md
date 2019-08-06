# Rock Paper Scissors:
- User input version w/ data collection & plotting.
- Generated data version, for each 3 choices, keeping each one fixed per run.
# User input version:
- By selecting a sensible number to loop the calculation, one can play vs the computer and collect data, to then plot a weighted histogram, showing the density of each event occuring ('Win','Lose','Tie','Invalid input').
# Random data generation, collection & plotting.
- By sellecting any number desired (depending on ram) one can perform a calculation, where either rock, paper or scissors is being kept constant as the users choice, and the computer has a randomly generated (varied seed) choice. 
- After perfrorming the calculation, which loops over rock, paper and scissors, the file is then saved in a folder (csv format).
- That file is then loaded and plotted in the same fashion as with the User input version, minus the 'Invalid input' response; As it only loops around the ('rock','paper','scissors') list.



Project inspired by Keith Galli:
https://github.com/KeithGalli/rockpaperscissors
