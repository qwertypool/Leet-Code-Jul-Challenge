# from collections import deque


# # Data structure to store a Binary Tree node
# class Node:
#     def __init__(self, key=None, left=None, right=None):

#         self.key = key
#         self.left = left
#         self.right = right

# ls = []
# # Function to print reverse level order traversal of given binary tree
# def reverseLevelOrderTraversal(root):
#     if root is None:
#         return

#     # create an empty queue and enqueue root node
#     queue = deque()
#     queue.append(root)

#     # create a stack to reverse level order nodes
#     stack = deque()

#     # run till queue is not empty
#     while queue:

#         # process each node in queue and enqueue their children
#         curr = queue.popleft()
# 		# print("curr = "+curr)
#         # push current node to stack
#         stack.append(curr.key)
#         #print(stack.pop(),end=" ")
#         if stack:
#             ls.append(stack.pop())
#         print("curr = ",curr.key)
#         # important - process right node before left node
#         if curr.right:
#             queue.append(curr.right)

#         if curr.left:
#             queue.append(curr.left)

#     # pop all nodes from the stack and print them
#     print(ls)
#     while stack:
#         print(stack.pop(), end=' ')


# if __name__ == '__main__':

#     root = Node(15)
#     root.left = Node(10)
#     root.right = Node(20)
#     root.left.left = Node(8)
#     root.left.right = Node(12)
#     root.right.left = Node(16)
#     root.right.right = Node(25)

#     reverseLevelOrderTraversal(root)
















# # Recursive Python program for level order traversal of Binary Tree 

# # A node structure 
# class Node: 

# 	# A utility function to create a new node 
# 	def __init__(self, key): 
# 		self.data = key 
# 		self.left = None
# 		self.right = None


# # Function to print level order traversal of tree 
# def printLevelOrder(root): 
# 	h = height(root) 
# 	for i in range(1, h+1):
# 		printGivenLevel(root, i) 

# ls = []
# # Print nodes at a given level 
# def printGivenLevel(root , level): 
# 	if root is None: 
# 		return
# 	elif level == 1: 
# 		print(root.data,end=" ")
#         #return ls.append(root.data) 
# 	elif level > 1 : 
# 		printGivenLevel(root.left , level-1) 
# 		printGivenLevel(root.right , level-1) 
#     #ls.append(root.data)

# """ Compute the height of a tree--the number of nodes 
# 	along the longest path from the root node down to 
# 	the farthest leaf node 
# """
# def height(node): 
# 	if node is None: 
# 		return 0
# 	else : 
# 		# Compute the height of each subtree 
# 		lheight = height(node.left) 
# 		rheight = height(node.right) 

# 		#Use the larger one 
# 		if lheight > rheight : 
# 			return lheight+1
# 		else: 
# 			return rheight+1

# # Driver program to test above function 
# root = Node(1) 
# root.left = Node(2) 
# root.right = Node(3) 
# root.left.left = Node(4) 
# root.left.right = Node(5) 

# print("Level order traversal of binary tree is -") 
# printLevelOrder(root) 

# #This code is contributed by Nikhil Kumar Singh(nickzuck_007) 


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