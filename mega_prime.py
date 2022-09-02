n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c>2:
    print("Not Mega Prime")
else:
    temp=n
    b=0
    while n:
        a=0
        r=n%10
        n=n//10
        for i in range(1,r+1):
            if r%i==0:
                a+=1
        if a==2:
            b+=1
    if b==len(str(temp)):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
            
                