def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(a)

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
                
arr = [64, 34, 25, 12, 57, 93, 1, 123]
d = [2, 4, 5, 1, 3]
bubblesort(arr)
sel_sort(d)
print(d)
print(arr)