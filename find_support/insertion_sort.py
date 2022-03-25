arr = [8, 4, 5, 3, 1, 2]

for i in range(len(arr)):
    for j in range(i,0,-1):
        if arr[j] < arr[j - 1]:
            arr[j] ,arr [j- 1] = arr[j-1], arr[j]
print(arr)