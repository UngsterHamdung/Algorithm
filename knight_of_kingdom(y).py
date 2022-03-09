# kn = input()
# kn = [ord(kn[0]) - 97, int(kn[1]) - 1]
# print(kn)
# count = 0
# for x, y in zip([-2, -2, 2, 2, -1, -1 ,1 ,1], [-1, 1, -1, 1, -2, 2, -2, 2]):
#     if [kn[0] + x, kn[1] + y] in [[i, j] for i in range(8) for j in range(8)]:
#         count += 1
# print(count)

[[i,j] for i in range(8) for j in range(8)]
