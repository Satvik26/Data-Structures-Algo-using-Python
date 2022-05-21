# We have a string and we need to replace all the "a" with "b"

#Code :

def replaceChar(s ,a , b):
     if len(s) == 0:
       return s
     smallerOutput = replaceChar( s[1:], a, b)
     if s[0] == a:
       return b+ smallerOutput
     else:
       return s[0]+ smallerOutput
  
 s = 'ababababab'

 print(replaceChar(s , 'a', 'b'))
