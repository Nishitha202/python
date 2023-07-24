def bin2Dec(val):
    rev=val[::-1]
    dec=0
    i=0
    for dig in rev:
        dec+=int(dig)*2**i
        i+=1
    return dec
num1=input("enter a binary number")
print(bin2Dec(num1))