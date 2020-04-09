def binary_search(arr, target):
    arr.sort()
    return b_search_func(arr, 0, len(arr) - 1, target)

def b_search_func(arr, start_index, end_index, target):
    # if start_index is less than end_index target was not found
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    
    if arr[mid_index] == target:
        return mid_index
    elif arr[mid_index] > target:
        return b_search_func(arr, start_index, mid_index - 1, target)
    else:
        return b_search_func(arr, mid_index + 1, end_index, target)
        
        
if __name__ == '__main__':
    arr = ['apple', 'peach', 'blueberry', 'cherry', 'lemon', 'key lime', 'rhubarb', 'chocolate creme']
    print(binary_search(arr, 'cherry'))
    print(binary_search(arr, 'rhubarb'))
    print(binary_search(arr, 'meat'))
    print('\n')
    arr2 = [2, 3, 9, 7, 4, 6, 8, 1, 25, 81, 96, 35, 5, 0, 774, 11]
    print(binary_search(arr2, 1))
    print(binary_search(arr2, 6))
    print(binary_search(arr2, 20))
    print(binary_search(arr2, 774))
