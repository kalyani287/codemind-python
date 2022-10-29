num=int(input())     
s=0
while num>0:
    r=num%10
    s+=r*r
    num=num//10
    if num==0 and s>9:
        num=s
        s=0
if s==1 or s==7:
    print(True)
else:
    print(False)
    
        
    