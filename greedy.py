n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n//coin
    print(count)
    n %= coin
    print(n)
print(count)
#시간 복잡도 1, logN, N, NlogN, N^2, N^3, 2^n

#당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 
#100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때
#거슬러 줘야 할 동전의 최소 개수를 구하라,
#단,거슬러 줘야할 돈 N은 항상 10의 배수

# n = 1260
# count = 0
# coin_types = [500, 100, 50, 10]

# for coin in coin_types:
#     count += n//coin
#     n %= coin
# print(count)

# 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을
# 종합해 다른 해가 나올 수 없기 때문이다.
#