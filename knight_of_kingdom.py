def dir_func1(a, b):
    return [(a+2, b+1), (a+2, b-1), (a-2, b+1), (a-2, b-1)]

def dir_func2(a,b):
    return [(a+1, b+2), (a-1, b+2), (a+1, b-2), (a-1, b-2)]

cur_loc = input()

row = ['1', '2', '3', '4', '5', '6', '7', '8']
column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

a = column.index(cur_loc[0])
b = row.index(cur_loc[1])

func1 = dir_func1(a,b)
func2 = dir_func2(a,b)
count = 0
for l in func1:
    if 0 <= l[0] <= 7 and  0 <= l[1] <= 7:
        count +=1  
for m in func2:
    if 0 <= m[0] <=7 and 0 <= m[1] <= 7:
        count+=1
print(count)
# board = []
# for  i in row:
#     for j in column:
#         board.append(str(j)+str(i))




#수평 2칸 수직 1칸 (2,-1) (-2,-1) (2,1) (-2, -1)
# 수직 2칸 수평 1칸 (1,-2) (-1,-2) (1, 2) (-1, 2)
# {} 이것의 형태와 얘의 활용 