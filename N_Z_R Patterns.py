#pattern N

# *       *
# * *     *
# *   *   *
# *     * *
# *       *

rows=int(input("Enter no.of rows to print N:"))
for i in range(rows):
    for j in range(rows):
        if j==0 or j==rows-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Z pattern

# * * * * *
#       *
#     *
#   *
# * * * * *

rows=int(input("Enter no.of rows to print Z:"))
for i in range(rows):
    for j in range(rows):
        if i==0 or i==rows-1 or i+j==rows-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#R pattern
# * * * * *
# *       *
# * * * * *
# *   *
# *     *
rows=int(input("Enter no.of rows to print R:"))
mid=rows//2
for i in range(rows):
    for j in range(rows):
        if j==0 or i==0 or i==mid or (j==rows-1 and i<mid) or (i>mid and i-j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        