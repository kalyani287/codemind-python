n=int(input())
l=[int(x) for x in input().split()]
a=0
for i in l:
    if i%2==0:
        a=i
print(a)