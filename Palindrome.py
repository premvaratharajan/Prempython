s = "radar"
b = "prem"

def isPalindrome(s):
    R = s[::-1]
    if R == s:
     return True;
    return False;

Ans = isPalindrome(s)

if Ans == 1:
   print "Given string radar is palindrome"
else:
   print "Given string radar is not a palindrome"   



