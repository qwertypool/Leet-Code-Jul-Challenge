def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #Here we can have different approaches:



        # Like the first one being a naive approach:
        ls = []
        while len(ls) != 1:
            temp = num
            ls = [int(i) for i in str(temp)]
            num = sum(ls)
            
        return num



        # Second approach using O(1) time & constant space:
        # if num == 0:
        #     return num
        # elif (num%9) == 0:
        #     return 9
        # else:
        #     result = num % 9
        #     return result
        

        #Or, by directly implementing the formula(O(1) time & space):
        # if num == 0:
        #     return num
        # else:
        #     result = 1 + ((num-1) % 9)
        #     return result
        
        