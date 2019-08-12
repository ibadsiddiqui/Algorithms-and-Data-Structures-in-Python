numbers = [1, 2, 3, 4, 5, 10, 7, 8, 9]

# random indexing -> O(1) get the items we know the index
# print(numbers[1])

# numbers[1] = "Adams"

# for item in numbers:
    # print(item)

# for i in range(len(numbers)):
    # print(numbers[i])

# print(numbers[:2])

# O(N) search running time
maximum_number = numbers[0]
for item in numbers:
    if maximum_number < item:
        maximum_number = item
print(maximum_number)
