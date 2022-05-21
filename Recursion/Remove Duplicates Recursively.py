"""
Remove Duplicates Recursively
Send Feedback
Given a string S, remove consecutive duplicates from it recursively.
Input Format :
String S
Output Format :
Output string
Constraints :
1 <= |S| <= 10^3
where |S| represents the length of string
Sample Input 1 :
aabccba
Sample Output 1 :
abcba
Sample Input 2 :
xxxyyyzwwzzz
Sample Output 2 :
xyzwz
"""

#Code :


def removeConsecutiveDuplicates(string):
    # Please add your code here
    n = len(string)
    if n == 0 or n==1:
        return string
    smallerOutput = removeConsecutiveDuplicates(string[1:])
    if string[0] == string[1]:
        return smallerOutput
    else:
        return string[0] + smallerOutput

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
