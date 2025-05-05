n=int(input())
start=97
for i in range(n):
    for j in range(i+1):
        if i==0 or j==0 or i==n-1 or i==j:
            print(chr(start),end=" ")
        else:
            print(" ",end=" ")
        start+=1
    print()