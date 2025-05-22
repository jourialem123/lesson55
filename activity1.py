def fun(n):
    sum=0
    for i in range(1,n+1):
     sum+=i
    return sum
print(fun(5))


#This is linear time complexity because we loop\repeat the code n times
#the symbol of it is: O(n)