def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] = freq[i]+1
            else:
                freq[i] = 1
        result = []
        for key,value in freq.items():
            if value==1:
                result.append(key)
        
        return result

print(singleNumber([1,2,1,3,2,5]))