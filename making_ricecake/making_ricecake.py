N, M = input().split()
length = list(map(int, input().split()))

def rice_cake(arr):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    count = max(arr)-min(arr)
    length_list = []
    for i in range(min(arr), max(arr), 1):
        for ele in arr:
            if (ele - i) >= 0: 
                length_list.append(abs(ele-i))
            else:
                length_list.append(0)
            if len(length_list) == 4:
                check = sum(length_list)
                length_list = []
                if check <= int(M):
                    return i
                else:
                    check = 0
plz = rice_cake(length)
print(plz)
