

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(node, result, level):
            if not node:
                return
            if len(result) < level + 1:
                result.append([node.val])
            else:
                result[level].append(node.val)
            dfs(node.left,  result, level + 1)
            dfs(node.right, result, level + 1)
            
        result = []
        dfs(root, result, 0)
        return result[::-1]
