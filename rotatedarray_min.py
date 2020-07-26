class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        #Simply return the minimum of nums LOLLL
        #return min(nums)
        
        #Or, a naive approach could be -----
        
        minimum = 99999
        if nums[0]< nums[len(nums)-1]:
            return nums[0]
        else:
            for i in nums:
                if minimum > i:
                    minimum = i
            return minimum
            
        