def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD is:", gcd(x, y))

f = open("sample.txt", "r")   # read mode

#read entire file
f = open("sample.txt", "r")
data = f.read()
print(data)
f.close()

#read one line at a time
f = open("sample.txt", "r")
print(f.readline())
print(f.readline())
f.close()

#read all line into a list
f = open("sample.txt", "r")
lines = f.readlines()
print(lines)
f.close()

#writes text(overwrite file)
f = open("sample.txt", "w")
f.write("Hello World\n")
f.write("Python is easy")
f.close()

#writes list of strings
f = open("sample.txt", "w")
lines = ["Line1\n", "Line2\n", "Line3\n"]
f.writelines(lines)
f.close()

#tells current position of cursor
f = open("sample.txt", "r")
print(f.tell())
f.read(5)
print(f.tell())
f.close()

#move cursor to position
f = open("sample.txt", "r")
f.seek(5)
print(f.read())
f.close()
