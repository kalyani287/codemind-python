n=int(input())
l=[int(x) for x in input().split()]
c=0
for i in l:
    if i%2==0:
        c+=1
if c==n:
    print(True)
else:
    print(False)