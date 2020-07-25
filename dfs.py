class Solution:
    def __init__(self):
        self.path=[]
        self.paths=[]
        
    def allPathsSourceTarget(self, graph):
        self.dfs(0, len(graph)-1, graph)
        return self.paths
    
    def dfs(self, i, final_point, graph):
        nodes = graph[i]
        self.path.append(i)
        if nodes:
            for n in nodes:
                if(n == final_point):
                    self.path.append(n)
                    self.paths.append(list(self.path))
                    self.path.pop(-1)
                else:
                    self.dfs(n, final_point, graph)
                    self.path.pop(-1)