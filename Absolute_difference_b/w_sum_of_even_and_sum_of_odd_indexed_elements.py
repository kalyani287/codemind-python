n=int(input())
l=[int(x) for x in input().split()]
even=odd=0
for i in range(0,len(l),2):
    even+=l[i]
for i in range(1,len(l),2):
    odd+=l[i]
print(abs(even-odd))