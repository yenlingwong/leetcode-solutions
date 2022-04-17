# Link: https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        '''
        answer = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    answer += node.val
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                
        return answer
        '''
        
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.answer += node.val
                if node.val > low:
                    dfs(node.left)
                if node.val < high:
                    dfs(node.right)
                
        self.answer = 0
        dfs(root)
        return self.answer
