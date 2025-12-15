arr = [1,2,0,3,4,5,0,0,6,7,8,0]

# output [1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0]

arr1 = []
arr2 = []

for i in arr:
    if i == 0:
        arr2.append(i)
    else:
        arr1.append(i)

print(arr1)
print(arr2)

# for this output [1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0] use this
arr1.extend(arr2)
print(arr1)

# for this output [0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8] use this
arr2.extend(arr1)
print(arr2)