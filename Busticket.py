start=input("enter the place1")
end=input("enter the place2")

def fn(start,end):
    if start=="Mangalore" and end=="Bangalore":
        return 200
    if start=="Manipal" and end=="kottara":
        return 300
    if start=="kuloor" and end=="suratkal":
        return 500

print(fn(start,end))
