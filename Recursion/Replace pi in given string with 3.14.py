def replacePi(s):
    n = len(s)
    if n==0 or n==1:
      return s
    if s[0] == 'p' and s[1] == 'i':
      smallerOutput = replacePi(s[2:])
      return "3.14" + smallerOutput
    else:
      smallerOutput = replacePi(s[1:])
      return s[0]+ smallerOutput
      
      
print(replacePi("pipipipeeesss"))
print(replacePi("dpipipeeesss"))
print(replacePi("peeesss"))

"""
Output
3.143.143.14peeesss
d3.143.14peeesss
peeesss 
"""
