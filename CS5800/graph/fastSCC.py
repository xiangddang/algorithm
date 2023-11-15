'''
Kosaraju and Sharir’s Algorithm
• Input: Adjacency list access to a directed graph G.
• Use DFS to get finishing times for all vertices.
• For each vertex u (in increasing order of finishing time):
     If u has already been marked, skip it.
     Use DFS to find C, the set of all unmarked vertices reachable from u.
     Mark the vertices of C.
     Add C to the output (this is the strongly connected component of u).
'''