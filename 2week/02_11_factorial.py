def factorial(n):
    if n == 1:   # 탈출 조건
        return 1
    return  n * factorial(n - 1)

print(factorial(5))