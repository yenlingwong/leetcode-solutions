# Link: https://leetcode.com/problems/find-all-the-lonely-nodes/

class Solution(object):
  def getLonelyNodes(self,root):
    values = []
    
    def dfs(node):
      if node:
          if not node.left and node.right:
            values.append(node.right.val)
            
          if node.left and not node.right:
            values.append(node.left.val)
          
          dfs(node.left)
          dfs(node.right)
     
    dfs(root)
    return values
            
    
