n=input()
ch=n[0]
cnt=1
s=1
res=""
while True:
    if n[s]==ch:
        cnt+=1
    else:
        res+=ch+str(cnt)
        ch=n[s]
        cnt=1
    if s==len(n)-1:
        res+=ch+str(cnt)
        break
    s+=1
print(res)