#1. Write a Python program to filter numbers divisible by 5 from a list of numbers.

def divby5(n):
    return n%5==0

n=list(map(int,input().split()))
lis1=list(filter(divby5,n))
print(lis1)

list1=list(filter(lambda x:x%5==0 ,n))
print(list1)


#2. Write a Python program to filter vowels from a string.

def vowels(i):
    return i in 'aeiouAEIOU'
stri=input()
lis1=list(filter(vowels,stri))
print("".join(lis1)) 