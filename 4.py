tup=("a","b","b","c","c","c","d","d","d","d")
s=set(tup)
l=[]
for x in s:
    c=list(tup).count(x)
    print(f"{x}:{c}")
    if c==1:
        l.append(x)
print("elements which ocurs only once:",l)