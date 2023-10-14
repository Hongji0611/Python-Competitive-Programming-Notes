# 피보나치 수
# F(n) = F(n-1) + F(n-2) 

def fibonacci_numbers(n):
    fibo = [0 for _ in range(n+1)]
    fibo[0] = 0
    fibo[1] = 1
    
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    
    return fibo[n]