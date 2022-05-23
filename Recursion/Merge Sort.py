'''
Merge Sort Code
Send Feedback
Sort an array A using Merge Sort.
Change in the input array itself. So no need to return or print anything.
Input format :
Line 1 : Integer n i.e. Array size
Line 2 : Array elements (separated by space)
Output format :
Array elements in increasing order (separated by space)
Constraints :
1 <= n <= 10^3
Sample Input 1 :
6 
2 6 8 5 4 3
Sample Output 1 :
2 3 4 5 6 8
Sample Input 2 :
5
2 1 5 2 3
Sample Output 2 :
1 2 2 3 5 
'''

# Code 1:

def merge(l1, l2 , a):
    i=0
    j=0
    k=0
    
    while  i< len(l1) and j<len(l2):
        if l1[i] <= l2[j]:
            a[k] = l1[i]
            k = k+1
            i = i+1
        else:
            a[k] = l2[j]
            k = k+1
            j = j+1
    
    while ( i < len(l1)):
        a[k] = l1[i]
        k = k+1
        i = i+1
    
    while ( j < len(l2)):
        a[k] = l2[j]
        k = k+1
        j = j+1


def mergeSort(arr):
    if len(arr)==0 or len(arr)==1:
        return 
    mid = len(arr) // 2
    l1 = arr[0:mid]
    l2 = arr[mid:]
    
    
    mergeSort(l1)
    mergeSort(l2)
    
    merge(l1,l2,arr)
    
# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)
