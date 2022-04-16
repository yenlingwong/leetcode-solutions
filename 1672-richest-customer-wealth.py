class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        maxwealth = 0
        wealth = 0
        i = 0
        
        while i < len(accounts):
            
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]
            
            if wealth > maxwealth:
                maxwealth = wealth
            
            wealth = 0
            i += 1
            
        
        return maxwealth
