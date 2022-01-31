# 첫째 줄에 N,M,K의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10,000이하의 수로 주어진다.
# 입력으로 주어지는 k는 항상 M보다 작거나 같다.
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

# 입력 예시              출력 예시
# 5 8 3                  46
# 2 4 5 4 6
n,m,k = map(int, input().split()) #map은 리스트의 요소를 지정된 함수로 처리해주는 함수
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
while True:
    for i in range(k):
        m += -1
        
        result += first
        if m == 0 :
            break
    m += -1
    result += second
    if m == 0:
        break
print(result)