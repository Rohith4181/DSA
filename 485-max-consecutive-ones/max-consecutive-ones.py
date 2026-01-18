class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxonescount =0
        count = 0 
        for i in nums:
            if (i == 1):
                count += 1
                maxonescount = max(maxonescount, count)
            else:
                count = 0
        return maxonescount            
        