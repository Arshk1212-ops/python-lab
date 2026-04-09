def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD is:", gcd(x, y))