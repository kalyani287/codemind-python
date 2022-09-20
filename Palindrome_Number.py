t=int(input())
for i in range(t):
    n=int(input())
    k=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    print(k==rev)