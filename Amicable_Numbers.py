m=int(input())
n=int(input())
s=0
p=0
for i in range(1,m):
    if (m%i)==0:
        s+=i
for j in range(1,n):
    if (n%j)==0:
        p+=j
if m==p and n==s:
    print('Amicable')
else:
    print('Not Amicable')
