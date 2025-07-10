input = 20

# 1. 1 1 2 3 5 8 13 ...
# 2. fibo(3) = fibo(2) + fibo(1) => 2 = 1 + 1

def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1
    
    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765