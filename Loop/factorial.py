# python program to find factorial

# input
n=int(input("enter number:"))
fact=1
# loop
for i in range(1,n+1):
    fact=fact*i
print("factorial of",n,"=",fact)
