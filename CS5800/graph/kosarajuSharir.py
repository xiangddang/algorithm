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
# geek for geek
class GFG:
    # dfs Function to reach destination
    def dfs(self, curr, des, adj, vis):
        # If current node is the destination, return True
        if curr == des:
            return True
        vis[curr] = 1
        for x in adj[curr]:
            if not vis[x]:
                if self.dfs(x, des, adj, vis):
                    return True
        return False
     
    # To tell whether there is a path from source to destination
    def isPath(self, src, des, adj):
        vis = [0] * (len(adj) + 1)
        return self.dfs(src, des, adj, vis)
     
    # Function to return all the strongly connected components of a graph.
    def findSCC(self, n, a):
        # Stores all the strongly connected components.
        ans = []
         
        # Stores whether a vertex is a part of any Strongly Connected Component
        is_scc = [0] * (n + 1)
         
        adj = [[] for _ in range(n + 1)]
         
        for i in range(len(a)):
            adj[a[i][0]].append(a[i][1])
         
        # Traversing all the vertices
        for i in range(1, n + 1):
            if not is_scc[i]:
                # If a vertex i is not a part of any SCC, insert it into a new SCC list
                # and check for other vertices whether they can be part of this list.
                scc = [i]
                for j in range(i + 1, n + 1):
                    # If there is a path from vertex i to vertex j and vice versa,
                    # put vertex j into the current SCC list.
                    if not is_scc[j] and self.isPath(i, j, adj) and self.isPath(j, i, adj):
                        is_scc[j] = 1
                        scc.append(j)
                # Insert the SCC containing vertex i into the final list.
                ans.append(scc)
        return ans
 
# Driver Code Starts
if __name__ == "__main__":
    obj = GFG()
    V = 5
    edges = [
        [1, 3], [1, 4], [2, 1], [3, 2], [4, 5]
    ]
    ans = obj.findSCC(V, edges)
    print("Strongly Connected Components are:")
    for x in ans:
        for y in x:
            print(y, end=" ")
        print()