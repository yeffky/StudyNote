# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(list1 + list2)

def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    while (low <= high):
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    s = [1, 2, 3, 4, 7, 9, 10, 18]
    res = binarySearch(s, 9)
    print(res)


