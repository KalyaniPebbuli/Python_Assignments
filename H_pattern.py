#task--1
#H pattern
print("H pattern")
n=int(input("Enter number of nows:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==(n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#task--2
#5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1 

print("Inverted Triangle Pattern with numbers")
n=int(input("Enter number of nows:"))
for i in range(n,0,-1):
    print((str(i)+" ")*i)

#task--3
# * * * * *
#  * * * *
#   * * *
#    * *
#     *


print("Traingle with stars")
n=int(input("Enter number of nows:"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print("*",end=" ")
    print()
