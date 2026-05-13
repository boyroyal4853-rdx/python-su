arr = [0, 1, 0, 3, 12]

result = []

zero_count = 0

for i in arr:

    if i != 0:
        result.append(i)

    else:
        zero_count += 1

for i in range(zero_count):

    result.append(0)

print(result)