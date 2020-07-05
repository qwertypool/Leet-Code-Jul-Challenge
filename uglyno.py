# def nthuglyNumberNumber(n):
#     count = 1
#     i = 2
#     while(count<n-1):
#         if i%2 == 0 or i%3 == 0 or i%5 == 0:
#             count = count + 1
#             print("Count = ",count)
#         i = i + 1
#         print("i = ",i)
#     return i

# # ans = nthuglyNumberNumber(1690)
# ans = nthuglyNumberNumber(10)
# print(ans)




# def nthuglyNumberNumber(n):
#     count = 2
#     i = 1
#     while count<n:
#         if i%2==0 or i%3==0 or i%5==0:
#             count+=1
#         i+=1
#         print("Count = ",count," i = ",i)
#     return i
            

# # ans = nthuglyNumberNumber(1690)
# ans = nthuglyNumberNumber(10)
# print(ans)

# def maxDivide( a, b ): 
#     while a % b == 0: 
#         a = a / b 
#     return a  
  
# # Function to check if a number  
# # is uglyNumber or not 
# def isuglyNumber( no ): 
#     no = maxDivide(no, 2) 
#     no = maxDivide(no, 3) 
#     no = maxDivide(no, 5) 
#     return 1 if no == 1 else 0
  
# # Function to get the nth uglyNumber number 
# def getNthuglyNumberNo( n ): 
#     i = 1
#     count = 1 # uglyNumber number count 
  
#     # Check for all integers untill  
#     # uglyNumber count becomes n 
#     while n > count: 
#         i += 1
#         if isuglyNumber(i): 
#             count += 1
#     return i 
  
# # Driver code to test above functions 
# no = getNthuglyNumberNo(1690) 
# print("150th uglyNumber no. is ", no)


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