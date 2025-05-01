#task2
rows=int(input())
cols=int(input())
for i in range(rows):
    for j in range(i+1):
        print(i+1,end=" ")
    print()