# check_point = []
# def find_pos(x, y, z):
#     count = 0
#     if[x,y]  not in  check_point:
#         check_point.append([x, y])  
#     for i in range(4):
#         index = i + z
#         if index >= 4:
#             index = (index)%4
#         c_x = x + cc_list[index][0]
#         c_y = y + cc_list[index][1]
        
#         if map_pos[c_x][c_y] == 0 and [c_x, c_y] not in check_point:
#             check_point.append([c_x,c_y])
#             find_pos(c_x,c_y, index)
#         else :
#             count += 1
#         if count == 4:
#             c_x = c_x + dir_case[index][1]
#             c_y = c_y + dir_case[index][0]
#             if map_pos[c_x][c_y] == 0:
#                 find_pos(c_x,c_y, index)
#             else:
#                 break
# r, c = map(int, input().split())
# pos_x, pos_y, dir = map(int, input().split())
# map_pos = []
# dir_case = {0 : [-1, 0], 1 : [0, -1], 2 : [1, 0], 3 : [0, 1]}
# cc_list = [[-1,0], [0,-1], [1,0], [0,1]]
# for i in range(r):
#     line = []              
#     for j in range(c):
#         line.append(0)     
#     map_pos.append(line)   
# for i in range(r):
#     map_pos[i] = list(map(int, input().split()))
# start_pos = map_pos[pos_x][pos_y]
# twist = dir_case[dir]
# twist = cc_list.index(twist)
# find_pos(pos_x, pos_y, twist)
# print(len(check_point))

from collections import deque # N, M을 공백을 기준으로 구분하여 입력 받기 
n, m = map(int, input().split()) # 2차원 리스트의 맵 정보 입력 받기 
graph = [] 
for i in range(n): 
    graph.append(list(map(int, input()))) 
    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우) 
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1] 
    # BFS 소스코드 구현 
    def bfs(x, y): 
        # 큐(Queue) 구현을 위해 deque 라이브러리 사용 
        queue = deque() 
        queue.append((x, y)) # 큐가 빌 때까지 반복하기 
        while queue: 
            print(queue)
            x, y = queue.popleft() # 현재 위치에서 4가지 방향으로의 위치 확인 
            for i in range(4): 
                nx = x + dx[i] 
                ny = y + dy[i] # 미로 찾기 공간을 벗어난 경우 무시 
                if nx < 0 or nx >= n or ny < 0 or ny >= m: 
                    continue # 벽인 경우 무시
                if graph[nx][ny] == 0: 
                    continue # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록 
                if graph[nx][ny] == 1: 

                    graph[nx][ny] = graph[x][y] + 1 
                    queue.append((nx, ny)) # 가장 오른쪽 아래까지의 최단 거리 반환 
        return graph[n - 1][m - 1] # BFS를 수행한 결과 출력 
        
print(bfs(0, 0))
