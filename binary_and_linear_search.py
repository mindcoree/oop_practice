
def quicksort(array):
    if len(array) < 2:
        return array
    pilot = array[0]
    greater = [i for i in array[1:] if i > pilot]
    less = [i for i in  array[1:] if i <= pilot]
    return less + [pilot] + greater


def binary_search(array,item):
    array = quicksort(array)
    low,high = 0,len(array)
    while high >= low:
        mid = (low + high) // 2
        if array[mid] > item:
            high = mid - 1
        elif array[mid] < item:
            low = mid + 1
        else:
            return mid
    return None


def linear_search(array,item):
    for idx in range(len(array)):
        if array[idx] == item:
            return idx
        else:
            return None


def func():
    ar = [5, 6, 2, 10]
    print(quicksort(ar))
    item = int(input('число которое хотим найти '))
    if binary_search(ar,item ):
        print(f"элемент:{item} находится под индексом: {binary_search(ar, item)}")
    else:
        print(f"Элемента {item} не существует в массиве")


func()



