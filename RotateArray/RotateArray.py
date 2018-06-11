
arr = [1,2,3]

def rotate_array_right(arr,n):
    for i in range(n):
        temp = arr.pop()
        arr.insert(0,temp)
    return arr

if __name__ == '__main__':
    print(rotate_array_right(arr,2))