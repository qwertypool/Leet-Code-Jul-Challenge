class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}
        a = 0
        ls = []
        for i in nums:
            if i in frequency:
                frequency[i]+= 1
            else:
                frequency[i] = 1
        for w in sorted(frequency, key=frequency.get, reverse=True):
            ls.append(w)
            
        return ls[0:k]
