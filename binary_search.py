def binary_search(arr, target):
    return b_search_func(arr, 0, len(arr) - 1, target)

def b_search_func(arr, start_index, end_index, target):
    # test for appropriate index order
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
    binary_search(arr, 'cherry')
    binary_search(arr, 'rhubarb')
    binary_search(arr, 'meat')
