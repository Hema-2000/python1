x=int(input("enter 1st number"))
y=int(input("enter 2nd number"))
print("addition: ",x+y)
print("subtraction: ",x-y)
print("Multiplication: ",x*y)
print("float div: ",x/y)
print("floor div: ",x//y)
print("power: ",x**y)
print("modulus: ",x%y)
print("Bitwise AND: ",x&y)
print("Bitwise OR: ",x|y)
print("Bitwise NOT: ",~x)
print("Bitwise XOR: ",x^y)
print("Bitwise ls: ",x<<2)
a=True
b=False
print(a and b)
print(a or b)
print(not a)
print(x<y)
print(x!=y)
x+=y
print("assignemnt for addition: ",x)
x*=y
print("assignemnt for multiploication: ",x)
z=int(input("enter 3rd value to compare"))
print(x is not y)
print (x is z)
list = [10, 20, 30, 40, 50]
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

