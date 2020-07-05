def getNthUglyNo(n): 
  
    uglyNumber = [0] * n
    uglyNumber[0] = 1
    i2 = i3 =i5 = 0

    mul_2 = 2
    mul_3 = 3
    mul_5 = 5
  
    for l in range(1, n): 
   
        uglyNumber[l] = min(mul_2, mul_3, mul_5) 
  
        if uglyNumber[l] == mul_2: 
            i2 = i2 + 1
            mul_2 = uglyNumber[i2] * 2
  
        if uglyNumber[l] == mul_3: 
            i3 =i3 + 1
            mul_3 = uglyNumber[i3] * 3
  
        if uglyNumber[l] == mul_5:  
            i5 =i5 +  1
            mul_5 = uglyNumber[i5] * 5
  
    return uglyNumber[-1] 
  
x = getNthUglyNo(1690)
print(x)