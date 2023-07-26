def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter a number"))
if num>=0:
    print("factorial(" ,num, ")=",fact(num),sep="")
else:
    print("error in input")
