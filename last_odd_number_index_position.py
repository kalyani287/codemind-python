n=int(input())
l=[int(x) for x in input().split()]
a=0
for i in range(0,n):
    if l[i]%2!=0:
        a=i
print(a)