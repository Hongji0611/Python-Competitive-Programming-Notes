import sys

input = sys.stdin.readline

# 행 또는 열이 홀수일 경우 모든 지점을 거칠 수 있음.
# 행과 열이 모두 짝수일 경우 i+j가 홀수인 지점을 제외하고 모두 탐색 가능.

r, c = map(int, input().split())
arr = []

for i in range(r):
    arr.append(list(map(int, input().split())))

result = ""

if r % 2 == 1:
    result += ("R" * (c - 1) + "D" + "L" * (c - 1) + "D") * (r // 2) + "R" * (c - 1)
elif c % 2 == 1:
    result += ("D" * (r - 1) + "R" + "U" * (r - 1) + "R") * (c // 2) + "D" * (r - 1)
elif c == 0:
    result += r * "D"
elif r == 0:
    result += c * "R"
elif r % 2 == 0 and c % 2 == 0:
    low = 1000
    position = [-1, -1]

    for i in range(r):
        for j in range(c):
            if (i + j) % 2 == 1:
                if low > arr[i][j]:
                    low = arr[i][j]
                    position = [i, j]
    
    result += ("D" * (r-1) + "R" + "U" * (r-1) + "R") * (position[1] // 2)

    #그래프 시작 위치 지정
    x = 2 * (position[1] // 2)
    y = 0
    xbound = x + 1

    while x != xbound or y != r - 1:
        if x < xbound and [y, x+1] != position:
            x += 1
            result += 'R'
        elif x == xbound and [y, x - 1] != position:
            x -= 1
            result += 'L'
        if y != r - 1:
            y += 1
            result += 'D'
        
    result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - (position[1] + 1)) // 2)

print(result)
