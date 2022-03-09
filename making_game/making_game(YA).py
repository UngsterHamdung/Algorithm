N ,M = map(int, input().split())
A, B, C = map(int, input().split())

NM = []
for _ in range(N):
    NM.append(list(map(int, input().split())))

direction = {0:[-1, 0], 3:[0, -1], 2:[1, 0], 1:[0, 1]}
ch = [A, B]
record = [ch]
rot = 0

while True:
    temp = [ch[i] + direction[C][i] for i in range(2)]
    if temp not in record and NM[temp[0]][temp[1]] == 0:
        ch = temp
        record.append(temp)
        rot = 0
    else:
        rot = rot + 1
        if rot == 4:
            ch = [ch[i] + direction[(C + 2)%4][i] for i in range(2)]
            rot = 0
            if NM[ch[0]][ch[1]] == 1:
                break
    print(C)
    C = (C+3) % 4

print(len(record))

# temp = [ch[i] + direction[C][i] for i in range(2)]
# if temp not in record and NM[temp[0]][temp[1]] == 0:
# ch = [ch[i] + direction[(C + 2)%4][i] for i in range(2)]