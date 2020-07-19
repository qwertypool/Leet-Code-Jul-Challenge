class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a,int_b = int(a,2),int(b,2)
        sum = int_a + int_b
        return bin(sum)[2:]