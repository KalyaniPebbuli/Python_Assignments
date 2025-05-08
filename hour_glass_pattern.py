#Task 1
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
rows=int(input("Enter the no.of rows:"))
for i in range(1,2*rows):
    cols=i if i<=rows else 2*rows-i
    for j in range(1,cols+1):
        print(j,end=" ")
    print()
    


##Task 2 Diamond Pattern

#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 
#  1 2 3 4 
#   1 2 3 
#    1 2 
#     1 


rows=int(input("Enter no.of rows to print diamond:"))
for i in range(1,2*rows+1):
    spaces=rows-i if i<=rows else i-rows
    cols=i if i<=rows else 2*rows-i
    for j in range(1,spaces+1):
        print(" ",end="")
    for j in range(1,cols+1):
        print(j,end=" ")
    print()

#Task 3
#hour_glass_pattern
# 1 2 3 4 5 
#  1 2 3 4 
#   1 2 3 
#    1 2 
#     1 
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

rows=int(input("enter no.of rows to print hour glass:"))
for i in range(1,2*rows):
    cols=rows-i+1 if i<=rows else i-rows+1
    spaces=i-1 if i<=rows else 2*rows-i-1
    print(" "*spaces,end="")
    for i in range(1,cols+1):
        print(i,end=" ")
    print()
    
    
#Task 4    
#pascal triangle
#    1
#   1 1
#  1 2 1
# 1 3 3 1
#1 4 6 4 1

rows=int(input("Enter no.of rows to print pascal triangle:"))
for i in range(rows):
    spaces=rows-i-1
    for j in range(spaces):
        print(" ",end="")
    c=1
    for j in range(i+1):
        print(c,end=" ")
        c=c*(i-j)//(j+1)
    print()