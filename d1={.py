d1={
    'science':[89,88,62,95],
    'language':[77,78,84,80]
    }
d2=list(d1.values())
d={}
for i in range(1,5):
    d[f"student{i}"]={
        "science":d2[0][i-1],
        "language":d2[1][i-1]
    }
print(d)