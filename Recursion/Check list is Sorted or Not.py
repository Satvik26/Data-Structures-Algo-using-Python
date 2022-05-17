# Code 1 : Using copy the list during function call

def issorted(li):
  n = len(li)
  if n==0 or n==1:
    return True
  if li[0] > li[1]:
    return False
  return sorted(li[1:])
  
  li = [1,2,3,40,5,6,7,8]
print(issorted(li))



# Code 2 : Using startIndex

def isSortedBetter(a, si):
  n = len(a)
  if si== n-1 or si==n:
    return True
  if a[si] > a[si+1]:
    return False
  return isSortedBetter(a , si+1)

a = [1,2,3,40,5,6,7,8]
print(isSortedBetter(a , 0))

