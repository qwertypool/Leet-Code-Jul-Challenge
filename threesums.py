class Solution(object):
    def threeSum(self, nums):
        k=0
        res=set()
        nums.sort()
        for i in range(len(nums)-2):
            const=nums[i]
            start=i+1
            stop=len(nums)-1
            while(stop>start): 
                if((nums[stop]+nums[start]+const)>k):
                    stop=stop-1
                elif((nums[stop]+nums[start]+const)<k):
                    start=start+1
                else:
                    res.add((const,nums[start],nums[stop]))
                    stop=stop-1
                    start=start+1
        return list(res)
        