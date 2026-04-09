d={}
s=input("Enter the string:")
for c in s:
    ch= c.lower()
    if ch==" ":
        continue
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
sorted_dict=dict(sorted(d.items()))
print(sorted_dict)