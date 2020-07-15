class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls1=[]
        ls = s.split(' ')
        for i in range(len(ls)-1,-1,-1):
            if ls[i].strip():
                ls1.append(ls[i])
        res = ' '.join(ls1)
        result = res.strip()
        return result