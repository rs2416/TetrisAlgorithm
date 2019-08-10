
## Challenge 
To design an python algorithm to solve the tetriling puzzle, with the objective of performing the **tiling as fast as possible** while **minimizing the sum of uncovered and added squares** in the targeted region. 
 
## Python files

##### *Main.py* 

Python file includes my algorithm, implementing graphs (adjacency lists), by expressing the target region as an undirected graph and the squares as nodes. Through the use of adjacency lists I was able to identify and approach the nodes/squares with the least edges/neighbours first, allowing me to have successful performance in comparison to the brute force method that I initially explored.

##### *Performance.py*

Python file allows one to set the size of the randomly generated target and outputs the performance of one's algorithm (accuracy and time performance).

 ```
 target = utils.generate_target(width=10, height=10, density=0.6)
 ```

##### *Utils.py*

Python file randomly generates an arbituary solvable target region.
