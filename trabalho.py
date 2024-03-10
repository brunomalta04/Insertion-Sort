def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

array = [50, 10, 21, 7, 9, 78, 36, 123]
insertion_sort(array)
print(array)

