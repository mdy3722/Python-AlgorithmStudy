# DP - 동적 계획법
# 이미 앞서 한 번 했던 일에 대해서 기록을 하여 재실행하지 않도록 하자
# memo라는 메모이제이션을 활용
# 메모이제이션에 없으면 값을 계산해서 메모이제이션에 추가
# fibo[5]가 memo에 없으니 fibo(4) + fifbo(3) 진행
# fibo(4)가 memo에 없으니 fibo(3) + fibo(2)
# fibo(3)이 없으니 fibo(2) + fibo(1) 진행 -> memo에 있다. 반환
# fibo(3) 계산됨 -> memo에 저장


input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    else:
        fibo_memo[n] = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
        return fibo_memo[n]
    

print(fibo_dynamic_programming(input, memo))