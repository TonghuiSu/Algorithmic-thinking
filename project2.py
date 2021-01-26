"""
BFS_visited algorithm and connected component(CC)
"""

#Use Python built-in module deque
from collections import deque 
import random

def bfs_visited(ugraph, start_node):
    """
    Use BFS to get the connected set from a starting node
    """
    queue = deque()
    visited = set() #Set is enough here.
    visited.add(start_node)
    queue.append(start_node)
    while len(queue) != 0:
        temp_node = queue.popleft()
        for neighbor in ugraph[temp_node]:   #In graph theory, neighborhood is 
            if neighbor not in visited:      #well defined, so could be used directely.
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def cc_visited(ugraph):
	"""
	Get a list of connected sets
	"""
	remaining_node = ugraph.keys()		#The keys are accessible directly.
	
	con_com = []  #connected component
	while len(remaining_node) != 0 :
		node = random.choice(remaining_node)
		visited = bfs_visited(ugraph,node)
		con_com.append(visited)
		for item in visited:
			remaining_node.remove(item)
	return con_com
	
	
def largest_cc_size(ugraph):
	"""
	Get the largest set in visited list
	"""
	total_list = cc_visited(ugraph)
	max_length_list = []
	for each_list in total_list:
		if len(max_length_list) < len(each_list):
			max_length_list = each_list
	return len(max_length_list)


def compute_resilience(ugraph, attack_order):
	"""
	Get Takes the undirected graph ugraph, a list of nodes attack_order 
	and iterates through the nodes in attack_order. 
	For each node in the list, the function removes the given node 
	and its edges from the graph and then 
	computes the size of the 
	largest connected component for the resulting graph.
	a list of largest cc size after k times attack
	"""
	list_of_largest_size = []
	list_of_largest_size.append(largest_cc_size(ugraph))
	#first thing is to add the max size of original graph.
	
	for node in attack_order:
		#delete each node in the attack list and corresponding edges
		#important operation for 'sets': how to remove edges. 
		for neighbor in ugraph[node]:
			ugraph[neighbor].remove(node)
		del ugraph[node]
		list_of_largest_size.append(largest_cc_size(ugraph))
	return list_of_largest_size
		