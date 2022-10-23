n=int(input())
m=str(n)
l=len(m)
temp=n
sum=0
rem=0
while temp>0:
    rem=temp%10
    sum=sum+int(rem**l)
    temp=temp//10
    l=l-1
if sum==n:
    print(True)
else:
    print(False)