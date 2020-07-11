class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ls=[]
        for i in range(0, len(nums) + 1):  
            for subset in itertools.combinations(nums, i):
                ls.append(list(subset))
        return ls