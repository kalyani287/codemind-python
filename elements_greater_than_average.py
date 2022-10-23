n=int(input())
l=[int(x) for x in input().split()]
s=0
a=len(l)
c=0
for i in l:
    s+=i
m=s//a
for i in l:
    if m<=i:
        c+=1
print(c)