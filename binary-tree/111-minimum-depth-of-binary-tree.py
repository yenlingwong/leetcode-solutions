# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Reference: Sai Anish Malla

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def minDepthBFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        # Check if binary tree exists
        
        deque = collections.deque()
        deque.append((root, 1))
        
        while deque:
            node, depth = deque.popleft()
            
            if not node.left and not node.right:
                return depth
            
            if node.left:
                deque.append((node.left, depth+1))
            
            if node.right:
                deque.append((node.right, depth+1))
                
    def minDepthDFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # From bottom to the top
        
        if not root:
            return 0
        # Check if current node exists
        
        if not root.left and not root.right:
            return 1
        # Check if current node is root node
        
        if not root.left and root.right:
            return 1 + self.minDepthDFS(root.right)
        
        if not root.right and root.left:
            return 1 + self.minDepthDFS(root.left)
        
        return 1 + min(self.minDepthDFS(root.left), self.minDepthDFS(root.right))
