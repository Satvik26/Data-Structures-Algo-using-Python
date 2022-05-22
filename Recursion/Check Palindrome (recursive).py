"""
Check Palindrome (recursive)
Send Feedback
Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
racecar
Sample Output 1:
true
Sample Input 2 :
ninja
Sample Output 2:
false
"""

# Code 1: By passing the copy of an array

def palindrome(s):
    n = len(s)
    if n == 0 or n==1:
        return True
    smallOutput = palindrome(s[1:n-1])
    if s[0] == s[n-1] and smallOutput == True:
        return True
    else:
        return False
    
    
s = str(input().strip())
if palindrome(s):
    print("true")
else:
    print("false")
    
 # Code 2: By using start and end Index


# si = start index  , ei = end index 

def helper(s , si , ei):
    
    if si == ei:
        return True
    if s[si] != s[ei]:
        return False
    if (si < ei):
        return helper(s, si+1 , ei-1)
    return True

def palindrome(s):
    n = len(s)
    
    if n==0 or n == 1:
        return True
    
    return helper(s , 0, n-1)
    
s = str(input().strip())
if palindrome(s):
    print("true")
else:
    print("false")
