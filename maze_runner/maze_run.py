# from collections import deque
# n, m = map(int, input().split())
# maze = []
# for _ in range(n):
#     maze.append(list(map(int, list(input()))))
# pos = [0, 0]
# real_path = deque()
# save_point = deque()
# dir = {0:[0, -1], 1:[1,0], 2:[0, 1], 3:[-1, 0]}
# def maze_escape(pos):
#     real_path.appendleft(pos)
#     save_point.appendleft(pos)
#     while(1):
#         for C in range(4):
#             go = [x + y for x,y in zip(pos,dir[C])]
#             print(go,str("tlqkf"))
#             if go[0] >= 0 and go[1] >= 0 and go[0] < n and go[1] < m:
#                 if maze[go[0]][go[1]] == 1 and go not in save_point:
#                     real_path.appendleft(go)
#                     save_point.appendleft(go)
#                     pos = go
#                 elif maze[go[0]][go[1]] == 0:
#                     continue
#         if go[0] == n -1 and go[1] == m-1:
#             return real_path 
# V = maze_escape(pos)
# print(V)
from collections import deque
N, M = map(int, input().split())
map_maze = []

for _ in range(N):
    map_maze.append(list(map(int, list(input()))))

pos = [0, 0]
dir = {0:[0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}
queue = deque()
check_list = []
max_row = N-1
max_col = M-1
def escape_maze(pos):
    go = 1
    queue = deque([pos])
    while queue:
        go +=1
        print(queue)
        hu = queue.popleft()
        for j in range(4):
            x = hu[0] + dir[j][0]
            y = hu[1] + dir[j][1]
            if x >= 0 and x < N and y >= 0 and y< M:
                if map_maze[x][y] == 1 and [x,y] not in check_list:
                    queue.appendleft([x,y])
                    check_list.append([x,y])   
            if x == N-1 and y == M-1:
                return go

V = escape_maze(pos)
print(V)