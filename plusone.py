def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = [str(i) for i in digits] 
        res = int("".join(s)) 
        sum = res + 1
        ls = [int(x) for x in str(sum)] 
        return ls
