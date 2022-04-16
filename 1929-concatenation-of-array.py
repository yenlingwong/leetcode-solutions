# Link: https://leetcode.com/problems/concatenation-of-array/

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        
        i = 0
        while len(ans) < 2 * len(nums):
            if len(ans) % len(nums) == 0:
                i = 0
            
            ans.append(nums[i])
            i += 1
        
        return ans
            
        
