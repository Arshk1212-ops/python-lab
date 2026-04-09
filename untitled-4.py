def pn(x):
    l=[]
    s=0
    for i in range(1,x):
        if x%i==0:
            l.append(i)
    for y in l:
        s+=y
    if s==x:
        return "Perfect number"
    else:
        return "Not a Perfect Number"

def hn(x):
    l=list(str(x))
    while x!=1 and x!=4:
        sum=0
        for n in l:
            sum+=int(n)**2
        x=sum
    if sum==1:
        print("happy number")
    elif sum==4:
        print("Not a happy number")
t=hn(203)
print(t)
        
    



