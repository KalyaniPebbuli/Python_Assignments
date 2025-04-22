
def vowels(i):
    return i in 'aeiouAEIOU'
stri=input()
lis1=list(filter(vowels,stri))
print("".join(lis1)) 