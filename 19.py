list1 = [[1, 2], [2, 4], [3, 5]]
list2 = [[3, 1], [1, 1], [2, 3]]

result = []

for i in range(len(list1)):
    row = []
    for j in range(len(list1[0])):
        row.append(list1[i][j] + list2[i][j])
    result.append(row)

print(result)


lists = [[1, 2, 3], [4, 5], [10, 1], [2, 2, 2]]

max_list = lists[0]
max_sum = sum(lists[0])

for lst in lists:
    if sum(lst) > max_sum:
        max_sum = sum(lst)
        max_list = lst

print("List with highest sum:", max_list)

nums = [-3, 5, -1, 8, -7, 2]

result = [0 if x < 0 else x for x in nums]

print(result)

words = ["racecar", "hello", "level", "world", "madam", "python"]

palindromes = [word for word in words if word == word[::-1]]

print(palindromes)

table = [[i * j for j in range(1, 5)] for i in range(1, 5)]

print(table)

d1 = {'excavation': 50000, 'paving': 120000}
d2 = {'paving': 80000, 'drainage': 60000}

result = {}

for key in d1:
    result[key] = d1[key]

for key in d2:
    if key in result:
        result[key] += d2[key]
    else:
        result[key] = d2[key]

print(result)

words = ["cat", "dog", "elephant", "ant", "bear"]

result = {}

for word in words:
    length = len(word)
    
    if length not in result:
        result[length] = []
    
    result[length].append(word)

print(result)

