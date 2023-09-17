from sys import maxsize
from itertools import permutations

V=4 #set amount of vertexes to be travled to, 
def travelsalesmen(graph,s) #makes use of a graph to denote the vertices that are visted and going to be visted, not including the starting opint until final permutation, and the weight of that path, 

    vertex= []

    # we must start at a specified node that starting pont will be a parameter for the loop to check, sice we must start there and end there, that ay the vertex will be noted for the path 
    for i in range(V):
        if i!=s:    
            vertex.append(i) 

    min_path=maxsize  
    next_permutation=permutations(vertex)

    # for loop for the next_permutation
    current_pathweight= 0

    k=s

    
    for j in i: 
       current_pathweight += graph[k][]
       current_pathweight += graph[k][s]


    if current_pathweight < min_path:   
        min_path=current_pathweight


    return min_path #best_i