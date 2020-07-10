def widthOfBinaryTree(self, root):
        if not root: 
            return 0 
        res = 0
        queue = [(root, 0)]
        while queue: 
            res = max(res, queue[-1][1] - queue[0][1] + 1)
            ls = []
            for node, i in queue: 
                if node.left:
                    ls.append((node.left, 2*i))
                if node.right: 
                    ls.append((node.right, 2*i+1))
            queue = ls
        return res 