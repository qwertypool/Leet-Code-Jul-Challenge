class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.adj_dict = defaultdict(set)
        for i, j in prerequisites:
            self.adj_dict[i].add(j)

        self.visited = [0] * numCourses
        self.result = []
        self.cycleFound = 0
        
        for i in range(numCourses):
            if self.cycleFound == 1: break      
            if self.visited[i] == 0:
                self.dfs(i)
     
        #return [] if self.cycleFound == 1 else self.result

        if self.cycleFound == 1:
            return []
        else:
            return self.result

    def dfs(self, start):
        if self.cycleFound == 1:
            return    
        if self.visited[start] == 1:
            self.cycleFound = 1               
        if self.visited[start] == 0:           
            self.visited[start] = 1             
            for neighbour in self.adj_dict[start]:   
                self.dfs(neighbour)
            self.visited[start] = 2             
            self.result.append(start) 