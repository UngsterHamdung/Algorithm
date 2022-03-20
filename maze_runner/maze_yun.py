N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))

move = {0:[1,0], 1:[0,1], 2:[-1,0], 3:[0, -1]} # 우, 하, 좌, 상

def bfs_run(start=[0, 0], end=[N-1, M-1]):
    visited = [start]
    que = [start]
    distance = 1
    while True:
        distance += 1
        temp = []
        print(que)
        for n in que:
            for C in range(4):
                node = [i+j for i, j in zip(n, move[C])]
                if 0 <= node[0] < N and 0 <= node[1] < M:
                    if graph[node[0]][node[1]] == 1 and node not in visited:
                        temp.append(node)
                        visited.append(node)
        if end in visited:
            return distance
        que = temp        
        
print(bfs_run())