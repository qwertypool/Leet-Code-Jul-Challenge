import math
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        c = -2*n
        
        discriminant = b*b - 4*a*c
        res = math.sqrt(discriminant) - b
        final = math.trunc(res // 2)
        
        return final