n=input()
smallest=""
for i in range(len(n)):
    temp=""
    for j in range(i,len(n)):
        temp+=n[j]
        if temp==temp[::-1]and len(temp)>1 and (smallest=="" or len(temp)<len(smallest)):
            smallest=temp
if smallest:
    print(smallest)
else:
    print("No palindrome found")
            