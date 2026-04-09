N=int(input("enter the number of items:"))
d={}
count=0
while True:
    if count!=N:
        item=input("enter the item:")
        price=int(input("enter its price:"))
        count+=1
    else:
        break
    d[item]=price
k=int(input("enter the number:"))
new_list1=list(d.keys())
new_list2=list(sorted(d.values()))
for product in d:
    if d[product]==new_list2[len(new_list1)-k]:
        print(f"{k} highest item is {product} with price of {new_list2[len(new_list1)-k]}")
    
