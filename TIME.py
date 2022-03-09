num = int(input())

count = 0
for h in range(num+1):
    for m in range(60):
        for s in range(60):
            temp_time = (str(h)+str(m)+str(s))
            
            for i in temp_time:
                if i == '3':
                    count += 1
                    break
print(count)