def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def run_loop(n,x):
    while is_prime(n)==False:
        n+=x
    return n
n=int(input())
pp=run_loop(n,-1)
np=run_loop(n,1)
if (n-pp)<(np-n):
    print(n-pp)
elif (n-pp)==(np-n):
    print(n-pp)
else:
    print(np-n)