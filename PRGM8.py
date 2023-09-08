class palistr:
    def __init__(self):
        self.palistr=False
    def chkpalindrome(self,mystr):
        if mystr==mystr[::-1]:
            self.palistr = True
        else:
            self.palistr = False
        return self.palistr

class paliInt(palistr):
    def __init__(self):
        self.paliInt=False

    def chkpalindrome(self, val):
        temp=val
        rev=0
        while temp!=0:
            dig=temp%10
            rev=(rev*10)+dig
            temp=temp//10
        if val==rev:
            self.paliInt=True
        else:
            self.paliInt=False
        return self.paliInt

st=input("enter the string")
stobj=palistr()
if stobj.chkpalindrome(st):
    print("given string is a palindrome")
else:
    print("given string is not a palindrome")

val=int(input("enter the integer"))
Intobj=paliInt()
if Intobj.chkpalindrome(val):
    print("given integer is a palindrome")
else:
    print("given  integer is not a palindrome")
