
arr = [-1,0,3,5,2,5,2]

def find_max_index (arr):
    max_index = 0
    for i in range(len(arr)):
        if arr[i] > max_index:
            max_index = i
    return max_index

if __name__ == '__main__':
    print(find_max_index(arr))
