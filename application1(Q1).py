"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import urllib.request
import matplotlib.pyplot as plt
import numpy as np


###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib.request.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.decode().split('\n')
    graph_lines = graph_lines[ : -1]
    
    print("Loaded graph with", len(graph_lines), "nodes")
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


#################################
#compute the in-degree data

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

citation_graph = load_graph(CITATION_URL)
normalized_graph = in_degree_distribution(citation_graph)

x = list(normalized_graph.keys())
y = list(normalized_graph.values())
plt.xscale('log')
plt.yscale('log')
plt.scatter(x,y)
plt.title("Normalized distribution of citations")
plt.xlabel('Citations')
plt.ylabel('Normalized distribution')
plt.xlim(1,10000)
plt.ylim(10**-5,1)
plt.show()
