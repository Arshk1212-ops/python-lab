N=int(input("Enter the number:"))
i=0
l=[]
while i<N:
    list=[]
    name=input("Enter the name:")
    marks=input("Enter the marks:")
    list.append(name)
    list.append(marks)
    l.append(list)
    i+=1
k=int(input("Enter the kth highest marks:"))
list_1=[]
for x in range (N):
    list_1.append(l[x][1])
list_1.sort(reverse=True)
for y in range (N):
    if l[y][1]==list_1[k-1]:
        print(f"{k} highest marks is {list_1[k-1]} got by {l[y][0]}")
    












