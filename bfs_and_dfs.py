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
Implement a recursive or iterative Depth first Search (DFS) algorithm to see if a path exists from (0, 0) to (n - 1, m - 1) which doesn't hit any obstacles

Task 2: 
Implement a Breadth First Search (BFS) algorithm to see if a path exists from (0, 0) to (n - 1, m - 1) and if a path exists, return the length of the shortest path.
If a path doesn't exist, return -1.

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



"""
from collections import deque #will need this for implementing Breadth First Search
from typing import List
class Solution:
    # return the list of all open neighbors
    def getNeighbors(self, position: List[int], grid: List[List[str]]) -> List[List[int]]:
        neighbors = []

        try:
            if grid[position[0] - 1][position[1]] == "*":
                neighbors.append([position[0] - 1, position[1]])
        except: pass

        try:
            if grid[position[0] + 1][position[1]] == "*":
                neighbors.append([position[0] + 1, position[1]])
        except: pass

        try:
            if grid[position[0]][position[1] - 1] == "*":
                neighbors.append([position[0], position[1] - 1])
        except: pass

        try:
            if grid[position[0]][position[1] + 1] == "*":
                neighbors.append([position[0], position[1] + 1])
        except: pass
        
        return neighbors

    #return True if path exists from (0, 0) to (n - 1, m - 1) otherwise return False
    def DFS(self, grid: List[List[str]]) -> bool:
        open = [[0, 0]] # row, col
        closed = []

        while len(open) > 0:
            temp = open.pop(0)
            closed.append(temp)

            if temp != [len(grid) - 1, len(grid[0]) - 1]: # if not goal
                neighbors = self.getNeighbors(temp, grid)

                for entry in neighbors:
                    if grid[entry[0]][entry[1]] == "*" and entry not in closed and entry not in open:
                        open.insert(0, entry)

            else:   # if goal
                return True

        return False

    #return -1 if there is no path from (0, 0) to (n - 1, m - 1) otherwise return the length of the shortest path
    def BFS(self, grid: List[List[str]]) -> int:
        open = [[0, 0, 0]] # row, col, depth
        closed = []

        while len(open) > 0:
            temp = open.pop(0)
            closed.append(temp[:2])

            if temp[:2] != [len(grid) - 1, len(grid[0]) - 1]: # if not goal
                neighbors = self.getNeighbors(temp, grid)

                for entry in neighbors:
                    if grid[entry[0]][entry[1]] == "*" and entry not in closed:
                        entry.append(temp[2] + 1)
                        open.append(entry)

            else:   # if goal
                return temp[2]

        return -1

def main():
    grid = [['*', '*', '*'],
            ['*', '#', '*'],
            ['*', '#', '*']]

    test = Solution()

    print(f"BFS: {test.BFS(grid)}")
    print(f"DFS: {test.DFS(grid)}")

if __name__ == "__main__":
    main()