# The fibonacci series that we consider is 1,1,2,3,5,8,13....... and so on.

def fibonacci(n):
    if n==1 or n== 2:
      return 1
    return fibonacci(n-1)+fibonacci(n-2)

n =  int(input())
fibonacci(n)  
