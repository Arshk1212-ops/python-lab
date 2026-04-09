def sum(a,b):
    sum=a+b
    return sum
def divide(a,b):
    divide=a/b
    return divide
def multiply(a,b):
    multiply=a*b
    return multiply
def minus(a,b):
    minus=a-b
    return minus
d={
    "+":sum,
    "-":minus,
    "/":divide,
    "*":multiply
}
a=int(input("Enter a:"))
b=int(input("Enter b:"))
op=input("enter operation:")
result=d[op](a,b)
print(result)