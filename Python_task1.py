def binary_search(array, start, end, xyz):
    if start<=end:
        mid = (start+end)//2
        if array[mid]==xyz:
            return mid
        elif array[mid]>xyz:
            return binary_search(array, start, mid, xyz)
        else:
            return binary_search(array, mid, end, xyz)
    else:
        return -1


input_array = input('Enter the array: ')
array_0 = input_array.split(' ')
array = []
for element in array_0:
    array.append(int(element))
vaiabl = int(input('Enter the element you are searching for: '))
array.sort()
print('Sorted Array:')
print(array)
result = binary_search(array, 0, len(array) - 1, vaiabl)

if result != -1:
    print(f"Element is present in the array at index {result}")
else:
    print("Can't find the required element")