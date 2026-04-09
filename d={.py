d={
    "name":"Alice",
    "Age":"20",
    "GPA":"8.75",
    "Year":"1",
    "City":"Trichy",
    "Fees":"9500.50"
}
for ch in d:
    if d[ch].isdigit():
        d[ch]=int(d[ch])
    elif "." in d[ch]:
        d[ch]=float(d[ch])

print(d)