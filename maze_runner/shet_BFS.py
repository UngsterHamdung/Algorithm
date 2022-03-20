# # graph = {
# #     'A': ['B'],
# #     'B': ['A', 'C', 'H'],
# #     'C': ['B', 'D'],
# #     'D': ['C', 'E', 'G'],
# #     'E': ['D', 'F'],
# #     'F': ['E'],
# #     'G': ['D'],
# #     'H': ['B', 'I', 'J', 'M'],
# #     'I': ['H'],
# #     'J': ['H', 'K'],
# #     'K': ['J', 'L'],
# #     'L': ['K'],
# #     'M': ['H']
# # }

# # def bfs(graph, start_node):
# #     visit = list()
# #     queue = list()

# #     queue.append(start_node)
# #     while queue:
# #         node = queue.pop(0)
# #         if node not in visit:
# #             visit.append(node)
# #             queue.extend(graph[node])

# #     return visit

# # visit = bfs(graph, 'A')
# # print(visit)

# check_dir = [[0]*4 for _ in range(5)]
# print(check_dir)
# for i in range(4):
#     check_dir[0][0].append(i)
# print(check_dir)
A = []
for i in range(5):

    for j in range(6):
        A[i][j] = 0
print(A[6][3])