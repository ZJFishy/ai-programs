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
from collections import deque
import heapq
from typing import List, Tuple
class Solution:
	# returns whether a grid point is in a given list
	def node_in(self, list: List[List[int]], coord: List[int]):
		for test_node in list:
			if test_node[3:5] == coord[3:5]: return test_node
		return False

	# returns the list of valid neighbors
	def moveGen(self, grid: List[List[str]], coord: List[int]) -> List[List[int]]:
		neighbors = []

		try: # check up if available
			if grid[coord[3] - 1][coord[4]] == "*" and coord[3] > 0:
				neighbors.append([coord[0], coord[1] + 1, coord[2] - 1, coord[3] - 1, coord[4], coord[3], coord[4]])
		except: pass

		try: # check down if available
			if grid[coord[3] + 1][coord[4]] == "*" and coord[3] < len(grid):
				neighbors.append([coord[0], coord[1] + 1, coord[2] - 1, coord[3] + 1, coord[4], coord[3], coord[4]])
		except: pass

		try: # check left if available
			if grid[coord[3]][coord[4] - 1] == "*" and coord[4] > 0:
				neighbors.append([coord[0], coord[1] + 1, coord[2] - 1, coord[3], coord[4] - 1, coord[3], coord[4]])
		except: pass

		try: # check right if available
			if grid[coord[3]][coord[4] + 1] == "*" and coord[4] < len(grid[0]):
				neighbors.append([coord[0], coord[1] + 1, coord[2] - 1, coord[3], coord[4] + 1, coord[3], coord[4]])
		except: pass
		
		return neighbors

	# returns the Manhattan length to the goal
	def heuristic(self, grid: List[List[str]], coord:List[int]) -> int:
		return abs(len(grid) - 1 - coord[0]) + abs(len(grid[0]) - 1 - coord[1])
	
	#return True if path exists from (0, 0) to (n - 1, m - 1) otherwise return False
	def a_star(self, grid: List[List[str]]) -> bool:
		open: List[List[int]] = [[int(0), int(0), int(0), int(0), int(0), int(0), int(0)]] # f(n), g(n), h(n), row, col, parent row, parent col
		heapq.heapify(open)
		closed = []

		while len(open) > 0:
			temp = heapq.heappop(open)
			closed.append(temp)

			if temp[3:5] == [len(grid) - 1, len(grid[0]) - 1]:
				return True

			else:
				successors = self.moveGen(grid, list(temp))

				for M in successors:
					if self.node_in(closed, M) != False:
						closed_node = self.node_in(closed, M)
						if temp[1] + 1 < closed_node[1]:
							closed_node[5:7] = temp[3:5]            # reassigning parent node
							closed_node[1] = temp[1] + 1            # recalculating g(n)
							closed_node[0] = sum(closed_node[1:3])	# recalculating f(n)

					elif self.node_in(open, M) != False:
						open_node = self.node_in(open, M)
						if temp[1] + 1 < open_node[1]:
							open_node[5:7] = temp[3:5]				# reassigning parent node
							open_node[1] = temp[1] + 1				# recalculating g(n)
							open_node[0] = sum(open_node[1:3])		# recalculating f(n)
					
					else:
						new = [0 for i in range(7)]
						new[2] = self.heuristic(grid, M)    		# assigning h(n)
						new[3:5] = M[3:5]                   		# assigning row and col
						new[5:7] = temp[3:5]                		# assigning parent row and parent col
						new[1] = temp[1] + 1                		# assigning g(n)
						new[0] = sum(new[1:3])              		# assigning f(n)
						heapq.heappush(open, new)
					
		return False

def main():
	grid = [['*', '*', '*'],
	   		['*', '#', '#'],
	   		['*', '#', '*']]
	s = Solution()
	print(s.a_star(grid))

if __name__ == "__main__":
	main()