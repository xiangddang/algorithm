#
# @lc app=leetcode id=2608 lang=python3
#
# [2608] Shortest Cycle in a Graph
#

# @lc code=start
from collections import defaultdict
from collections import deque
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for v, w in edges:
            G[v].append(w)
            G[w].append(v)
        self.res = float('inf')
        def bfs(v):
            level = defaultdict(int)
            visited = set()
            que = deque([(v,0)])
            while que:
                v, d = que.popleft()
                if v in visited: continue
                visited.add(v)
                level[v] = d
                parents = set()
                for w in G[v]:
                    if w in visited:
                        if level[w] == d-1:
                            parents.add(w)
                            if len(parents) == 2:
                                self.res = min(self.res, 2*d)
                                return
                        if level[w] == d:
                            self.res = min(self.res, 2*d + 1)
                    else:
                        que.append((w,d+1))
        for v in range(n):
            bfs(v)
        return self.res if self.res != float('inf') else -1
                            
# @lc code=end

