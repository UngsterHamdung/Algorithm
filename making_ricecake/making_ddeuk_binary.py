N, M = input().split()
ddeuk = list(map(int, input().split()))
start = 0
ddeuk.sort()
end = max(ddeuk)

while start <= end:
    mid = (start + end) // 2
    check = []
    for ele in ddeuk:
        leftover = ele - mid
        if (leftover) >= 0:
            check.append(leftover)
        else:
            check.append(0)
    checkpoint = sum(check)
    if checkpoint == int(M):
        answer = mid
        break
    elif checkpoint > int(M):
        start = mid + 1
    else: 
        end = mid - 1 
print(answer)