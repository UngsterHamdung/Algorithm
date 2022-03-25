import sys
N = input()
original_data = list(map(int, input().split()))
M = input()
find_data = list(map(int, input().split()))

def binary_search(array, target, start, end):
        while start <= end:
            mid = (start + end) // 2

            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return None
correct_list = []
for i in range(int(M)):
    if binary_search(original_data, find_data[i], 0, int(N) - 1):
        correct_list.append("yes")
    else:
        correct_list.append("no")
print(correct_list)