n, m = map(int, input().split())

result = 0

if n == 1 or m == 1:
    print(1)
elif n == 2:
    print(min(4, (n-1)//2+1))
elif m <= 7:
    print(min(4, m))
else:
    print((m-5)+3)