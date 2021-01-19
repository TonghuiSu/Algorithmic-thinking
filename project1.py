"""
first part is to get three default graphs
"""

EX_GRAPH0={0:set([1,2]),1:set([]),2:set([])}
EX_GRAPH1={0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),
          4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2={0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),
          4:set([1]),5:set([2]),6:set([]),7:set([3]),
          8:set([1,2]),9:set([0,3,4,5,6,7])}


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

def compute_in_degrees(digraph):
    """
    after getting a digraph, convert to get the number of head nodes
    """
    num_in_degree = {}
    for node in digraph:
        num_in_degree[node]=0			#set the return dictionary.
   
    
    for node in digraph:
        for item in digraph[node]:
            num_in_degree[item] +=1
    
    return num_in_degree


def in_degree_distribution(digraph):
    """
    get the in degree distribution
    """
    degree_distribution = {}
    for num in range(0,len(digraph)):
        degree_distribution[num] = 0
    
    in_degree = compute_in_degrees(digraph)
    for item in in_degree:
        degree_distribution[in_degree[item]] +=1
        
    for num in range(0,len(digraph)):
        if degree_distribution[num] == 0:
            del degree_distribution[num]
            
    return degree_distribution