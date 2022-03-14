
N, M = map(int, input().split())
tray = [[0]*N for _ in range(N)]
cur_tray = []

real_tray = [[0]*M for _ in range(N)]
for _ in range(N):
    cur_tray.append(list(map(int, list(input()))))
# print(real_tray)
dir = [ [-1, 0], [0, -1], [1, 0], [0, 1]]

def dfs(list, x, y, visited = []):
    visited.append([x, y]) 
    for j in range(len(dir)):
        pos_x = x + dir[j][0]
        pos_y = y + dir[j][1]  
        if pos_x >= 0 and pos_x < N and pos_y>=0 and pos_y <M:
            if list[pos_x][pos_y] == 0 and [pos_x, pos_y] not in visited :      
                dfs( cur_tray, pos_x, pos_y, visited)
    return visited

visited = []
count = 0
# visited = dfs(cur_tray, 0, 0, visited)
for i in range(N):
    for j in range(M):
        if [i, j] not in visited and cur_tray[i][j] == 0:
            visited = dfs(cur_tray, i, j, visited)
            count +=1
print(count)

# N, M = map(int, input().split())
# tray = [[0]*N for _ in range(N)]
# real_tray = [[0]*M for _ in range(N)]

# cur_tray = []
# for _ in range(N):
#     cur_tray.append(list(str(input())))

# dir_case = [[-1, 0], [0, -1], [1, 0], [0, 1]]
# pos_x = 0
# pos_y= 0
# c = 0
# def dfs(base = cur_tray, pos_x, pos_y, visited):
   
#     if cur_tray[pos_x][pos_y] == '0' and real_tray[pos_x][pos_y] == False:
#         real_tray[pos_x][pos_y] = True
#         if pos_x <= -1 or pos_x >= N or pos_y <= -1 or pos_y >= M:
#             pos_x = pos_x + dir_case[c][0]
#             pos_y = pos_y + dir_case[c][1] 
#     c +=1
#     if c == 4:
#         c = c%4


# print(real_tray)