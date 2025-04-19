import numpy as np
import time


# Создание массива из 5000 элементов
rand_array = np.random.randn(5000)
q_array = np.copy(rand_array)
b_array = np.copy(rand_array)
m_array = np.copy(rand_array)
def quick_sort(array):
    if array.size < 2:
        return array

    pilot = np.random.choice(array)
    less = np.array([arr for arr in array if arr <= pilot])
    greater = np.array([arr for arr in array if arr > pilot])
    equal = np.array([arr for arr in array if arr == pilot])

    return np.concatenate((quick_sort(less), equal, quick_sort(greater)))

def merge(left, right):
    result = np.empty(left.size + right.size)  # выделение памяти
    i = j = k = 0
    # слияние
    while i < left.size and j < right.size:
        if left[i] < right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    # добавляем оставшиеся элементы из left и right, если они есть
    while i < left.size:
        result[k] = left[i]
        k += 1
        i += 1

    while j < right.size:
        result[k] = right[j]
        k += 1
        j += 1

    return result

def merge_sort(array):
    if array.size <= 1:
        return array

    mid = array.size // 2

    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)



def bubble_sort(array):
    n = array.size
    for i in range(n):
        swapped = False
        for j in range(0,n - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break


    return array


def time_sort(func, array):
    start_time = time.time()
    func(array)
    end_time = time.time()
    result_time = end_time - start_time
    return result_time




# Измеряем время для каждого алгоритма
q_time = time_sort(quick_sort,q_array)
b_time = time_sort(bubble_sort,b_array)
m_time = time_sort(merge_sort,m_array)
print(f"Время Quick sort: {q_time}")
print(f"Время Bubble sort: {b_time}")
print(f"Время Merge sort: {m_time}")
