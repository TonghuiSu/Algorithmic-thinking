"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random
import matplotlib.pyplot as plt
import numpy as np


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    
####################################
#make the initial complete graph.

def make_complete_graph(num_nodes):
    """
    try to get the complete graph
    """
    complete_graph = {}
    for num in range(0,num_nodes):
        complete_graph[num]=set([])
        for item in range(0,num_nodes):
            if item != num:
                complete_graph[num].add(item)
    
    return complete_graph

def DPA(initial_number,final_number):
    """
    This is for forming DPA graph.
    """
    
    #First, form the initial complete graph.
    dpa_graph = make_complete_graph(initial_number)
    
    #Second, use DPATrial to append new nodes to the dpa_graph.
    trial_graph = DPATrial(initial_number)
    for item in range(initial_number,final_number):
        dpa_graph[item] = trial_graph.run_trial(initial_number)
    
    return dpa_graph


#################################
#compute the in-degree nodes.

def compute_in_degrees(digraph):
    """
    after getting a digraph, convert to get the number of head nodes
    """
    num_in_degree = {}
    for node in digraph:
        num_in_degree[node]=0           #set the return dictionary.
   
    
    for node in digraph:
        for item in digraph[node]:
            num_in_degree[item] +=1
    
    return num_in_degree


###############################
#get the distribution of each nodes(but not normalized)

def in_degree_distribution(digraph):
    """
    get the in degree distribution
    """
    degree_distribution = {}        #the dictionary that returns with distribution.
    total_num = 0                   #The total edges in this graph.(for normalize)
    
    for num in range(0,len(digraph)):
        degree_distribution[num] = 0
    
    in_degree = compute_in_degrees(digraph)
    for item in in_degree:
        degree_distribution[in_degree[item]] +=1
        total_num += 1

    total_num -= degree_distribution[0]
    del degree_distribution[0]
    
    for num in range(1,len(digraph)):           #delete nodes with zero inputs and normalize non-zero nodes.
        if degree_distribution[num] == 0:
            del degree_distribution[num]
        else:
            degree_distribution[num] = degree_distribution[num]/total_num
            
    return degree_distribution
    
##############################
#make a plot for normalized distribution.

initial_graph = DPA(13,27770)
normalized_graph = in_degree_distribution(initial_graph)

x = list(normalized_graph.keys())
y = list(normalized_graph.values())
plt.xscale('log')
plt.yscale('log')
plt.scatter(x,y)
plt.title("Normalized distribution of ER method")
plt.xlabel('Nodes')
plt.ylabel('Normalized distribution')
plt.xlim(1,10000)
plt.ylim(10**-5,1)
plt.show()
