l=[]
while True:
    x=input("Enter the number:")
    if x !="s":
        l.append(int(x))
    else:
        break
l_2=set()
for i in l:
    for j in l:
        for k in l:
            for m in l:
                if i*j==k*m and i!=j and j!=k and k!=m and m!=i and m!=j and i!=k:
                    l_1=(i,j,k,m)
                    l_2.add(l_1)
                    
    
print((l_2))
