class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        """
        def ans(node, result, height):
            if not node:
                return
            if len(result) < height + 1:
                result.append([node.val])
            else:
                result[height].append(node.val)
            ans(node.left,  result, height + 1)
            ans(node.right, result, height + 1)
            
        result = []
        ans(root, result, 0)
        return result[::-1]