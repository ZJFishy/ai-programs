"""
Input:

We are given an n x m array called grid where 1 <= n <= 10 ** 3 and 1 <= m <= 10 ** 3.
Each entry of the grid is marked with a '*' or a '#'. '#' represent obstacles. So for all i and j, 
grid[i][j] = '*' or '#'. It is also guaranteed that grid[0][0] = '*'.
We initially start at position (0, 0) and we would like to move to position (n - 1, m - 1). 
We are only allowed to move to an adjacent square on the grid which isn't marked with an obstacle. 
Specifically if we are located at a position (i, j), we can move to a position (u, v) which is located to 
the immediate left, right, top, or bottom of position (i, j) if 0 <= u < n - 1 and 0 <= v < m - 1 and grid[u][v] = '*'

Task 1: 
Implement an A* algorithm which finds the shortest path between position (0, 0) and (n - 1, m - 1).
Your heuristic can be anything that you like


Inputs for all of these functions will be the same. 
Example testcases:
====================================================================================
Testcase 1

Input:
grid = [['*', '*', '*'],
       ['*', '#', '#'],
       ['*', '#', '*']]

DFS output: False
BFS output: -1
__________________________________
Testcase 2

Input:
grid = [['*', '*', '*'],
       ['*', '#', '*'],
       ['*', '#', '*']]

DFS output: True
BFS output: 4

__________________________________
Testcase 3

Input:
grid = [['*']]

DFS output: True
BFS output: 0

Explanations: 

For testcase 1, there is no path from (0, 0) to (2, 2) which doesn't hit an obstacle '#', so DFS returns False and BFS returns -1

For testcase 2, the shortest path from (0, 0) to (2, 2) is (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2) which is of length 4

For testcase 3, we are looking for the shortest path from (0, 0) to (0, 0) which is of length 0

The testcases will be randomly generated with each cell in the grid (except (0,0) and (n-1, m-1)) having a 10%
chance of being filled. (You don't have to use this 10% number to get some very specific heuristic
which happens to work extremely well, just come up with a few heuristics and pick the best of these )
"""
from collections import deque, heapq
from typing import List
class Solution:
    # returns the diagonal length to the goal
    def heuristic(self, grid: List[List[str]], coord:List[int]) -> int:
        return ((len(grid) - coord[0]) ** 2 + (len(grid[0]) - coord[1]) ** 2) ** 0.5
    
    #return True if path exists from (0, 0) to (n - 1, m - 1) otherwise return False
    def a_star(self, grid: List[List[str]]) -> bool:
        #IMPLEMENT ME
        pass
    