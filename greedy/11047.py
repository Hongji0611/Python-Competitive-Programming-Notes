n, cost = map(int, input().split())

coin = list()
for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

count = 0
for c in coin:
    count += cost // c
    cost = cost % c

print(count)
