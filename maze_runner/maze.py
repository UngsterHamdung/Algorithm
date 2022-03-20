# from collections import deque
# from re import X
# N, M = map(int, input().split())
# map_maze = []
# for _ in range(N):
#     map_maze.append(list(map(int, list(input()))))
# pos = [0, 0]
# dir = {0:[0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}
# dont_go = []
# queue = deque()
# cur_dir = []
# def escape_maze(scale, pos, visited):
#     if pos[0] == N-1 and pos[1]== M-1:
#         return visited
#     if pos[0] >= 0 and pos[1] >= 0 and pos[0] < N and pos[1] < M:
#         for C in range(4):
#             case = [x+y for x,y in zip(pos, dir[C])]
#             if scale[case[0]][case[1]] == 1 and pos not in visited and C != cur_dir[-1]:
#                 visited.append(case)
#                 if cur_dir:
#                     cur_dir.pop()
#                 cur_dir.append(C)
#                 escape_maze(scale, case, visited)
#             elif scale[case[0]][case[1]] == 0 and visited:
#                 pos = visited.pop()
#                 escape_maze(scale, pos, visited)


                        
# V = escape_maze(map_maze, pos, queue )
# print(V)


from collections import deque
N, M = map(int, input().split())
map_maze = []

for _ in range(N):
    map_maze.append(list(map(int, list(input()))))

pos = [0, 0]
dir = {0:[0, -1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}
queue = deque()

real_path = [[0]*M for _ in range(N)]

def escape_maze(pos):
    queue = deque([pos])
    real_path[pos[0]][pos[1]] = True
    queue.append(pos)
    way_point = []
    way_point.append(pos)

    while(1):
        temp = []
        v = queue.popleft()
        
        for C in range(4):
            temp.append([x+y for x,y in zip(v, dir[C])])
        for go in temp:
            if go[0] == N-1 and go[1] == M-1:
                return real_path, way_point
            if go[0] >= 0 and go[0] < N and go[1] >=0 and go[1] < M:
            
                if map_maze[go[0]][go[1]] == 1 and go not in way_point:
                    queue.append(go)
                    real_path[go[0]][go[1]] = True
                    print(queue)
                    way_point.append(go)

                elif map_maze[go[0]][go[1]] == 0:
                    continue 
        
        C += 1
        if C == 4:
            C = C % 4
                        
V, Y = escape_maze(pos)
print(V, Y)