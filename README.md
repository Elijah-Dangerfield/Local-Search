# Local Search

This project is an excercise from CSCI 4350: Introduciton to Artificial Intelligence. The goal of this project is to explore the 
performance in different methods of local search for problem solving. 

Both algorithms tested were tasked to search for maxima in a randomly generated space using the Sum of Gaussians function both with the same random starting point. 
Each algorithm was tested with every combination of  
N = {10 , 50 , 100, 1000 }   
D = { 1, 2, 3, 5}   
where N is the number of Gaussians (hills) and D is the dimension, for 100 runs each with a different random seed for a total of 3200 runs (1600 each).


## The two search methods: 

## Greedy Hill Climbing
found in greedy.py

This method of search uses a simple gradient ascent method to finding a maxima. 

## Simulated Annealing 
found in sa.py

This method uses simulated annealing with a starting tempurature of 10,000 and a cooling tempurature of .99

# Results
The statistics and exact result can be round in ```report.pdf```
The results show that simulated annealing generally outperformed greedy hill climbing in lower dimensions 
and with a lower number of gaussians. However, greedy hill climbing performed better than simulated annealing
with a higher number of gaussians

