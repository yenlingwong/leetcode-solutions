class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        runningSum = []
        i = 0
        
        while i < len(nums):
            if i == 0:
                runningSum.append(nums[i])
            
            else:            
                runningSum.append(nums[i] + runningSum[i-1])
            
            i += 1
        
        return runningSum
