#if-elif
'''
a=int(input("enter  first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))


if a>=b and a>=c:
    print(a," is the largest number")
elif b>=c and b>=a:
    print(b ,"is the largest number")
else:
     print(c, "is the largest number")
'''

# max() function
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))

largest=max(a,b,c)
print("The largest number is: ",largest)

