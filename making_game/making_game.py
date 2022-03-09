check_point = []
def find_pos(x, y, z):
    count = 0
    if[x,y]  not in  check_point:
        check_point.append([x, y])  
    for i in range(4):
        index = i + z
        if index >= 4:
            index = (index)%4
        c_x = x + cc_list[index][0]
        c_y = y + cc_list[index][1]
        
        if map_pos[c_x][c_y] == 0 and [c_x, c_y] not in check_point:
            check_point.append([c_x,c_y])
            find_pos(c_x,c_y, index)
        else :
            count += 1
        if count == 4:
            c_x = c_x + dir_case[index][1]
            c_y = c_y + dir_case[index][0]
            if map_pos[c_x][c_y] == 0:
                find_pos(c_x,c_y, index)
            else:
                break
r, c = map(int, input().split())
pos_x, pos_y, dir = map(int, input().split())
map_pos = []
dir_case = {0 : [-1, 0], 1 : [0, -1], 2 : [1, 0], 3 : [0, 1]}
cc_list = [[-1,0], [0,-1], [1,0], [0,1]]
for i in range(r):
    line = []              
    for j in range(c):
        line.append(0)     
    map_pos.append(line)   
for i in range(r):
    map_pos[i] = list(map(int, input().split()))
start_pos = map_pos[pos_x][pos_y]
twist = dir_case[dir]
twist = cc_list.index(twist)
find_pos(pos_x, pos_y, twist)
print(len(check_point))