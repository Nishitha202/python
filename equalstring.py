str1=input("enter string1")
str2=input("enter string2")
if len(str2)<len(str1):
    short=len(str2)
    long=len(str1)
else:
    short=len(str1)
    long = len(str2)
matchCnt=0
for i in range(short):
    if str1[i]==str2[i]:
        matchCnt+=1
print("similarity b/w  2 strings")
print(matchCnt/long)