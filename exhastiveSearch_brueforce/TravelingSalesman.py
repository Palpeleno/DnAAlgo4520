from sys import maxsize
from itertools import permutations

V=4 #set amount of vertexes to be travled to, 

def travelingsalesmen(graph,s) #makes use of a graph to denote the vertices that are visted and going to be visted, not including the starting opint until final permutation, and the weight of that path, 

    vertex= []
    # we must start at a specified node that starting point will be a parameter for the loop to check,
    # since we must start there and end there, that at the vertex will be noted for the path
    # as long as the iterative value dosent equal the amount of node the loop will continue
    for i in range(V):
        if i!=s:    
            vertex.append(i) 

    min_path = maxsize  
    next_permutation = permutations(vertex)

    # for loop for the next_permutation, going to the next vertext/node in the graph
    for i in next_permutation:
        print(i)
        current_pathweight= 0
        
        k=s
        for j in i: 
            current_pathweight += graph[k][j]
            k = j
            current_pathweight += graph[k][s]

        if current_pathweight < min_path:   
            min_path = current_pathweight
            best_i = i
    return min_path #best_i

#driver 
#the graph simulate the distance to each node 
graph = [[0,10,15,20],
         [10,0,35,25],
         [15,35,0,30],
         [20,25,30,0]]

s = 0
print(travelingsalesmen(graph, s))