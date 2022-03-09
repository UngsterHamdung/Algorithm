scale = int(input())
data = list(map(str, input().split()))

basic_hor = 1
basic_ver = 1

for i in data:
    
    if i == 'R' and basic_hor < scale :
        basic_hor += 1
    elif i == 'L' and basic_hor > 1:
        basic_hor -= 1
    elif i == 'U' and basic_ver > 1:
        basic_ver -= 1
    elif i == 'D' and basic_ver < scale:
        basic_ver += 1
print(basic_ver, basic_hor)   

