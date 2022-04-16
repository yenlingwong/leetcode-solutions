# Link: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node):
            if node:
                values.add(node.val)
                dfs(node.left)
                dfs(node.right)
            
        values = set()
        dfs(root)
        
        minimum = root.val
        ans = float('inf')
        
        for value in values:
            if value > minimum and value < ans:
                ans = value
        
        return ans if ans < float('inf') else -1
