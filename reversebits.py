# def reverseBits(n):
#     ls=[int(i) for i in n]
#     ls1=[]
#     l=len(ls)
#     string=""
#     for i in range(l-1,0,-1):
#         ls1.append(ls[i])
#     ls1=[str(i) for i in ls1]
#     string=string.join(ls1)
#     i=int(string)
#     return i

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        power = 31
        while n:
            res += (n & 1) << power
            n = n >> 1
            power -= 1
        return res
