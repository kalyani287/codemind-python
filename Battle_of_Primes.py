def prime(u):
    f=0
    for i in range(1,u+1):
        if u%i==0:
            f+=1
    if f==2:
        return True
    else:
        return False
def nxprime(u):
    while prime(u)==False:
        u=u+1
    return u
n=int(input())
m=int(input())
a=n+m
p=nxprime(a)
if prime(a)==True:
    p=nxprime(a+1)
    print(p-a)
else:
    print(p-a)