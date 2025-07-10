input = 20

# 소수들로 나누어떨어지는 지만 보자 - 전체 숫자로 나눠보지 말고..
# 그 중에서도 n의 제곱근까지만 보자 - ex) 16 = 4 * 4, 2 * 8, 1 * 16 -> 즉 곱하기 형태의 두 피연사 중
# 한 쪽은 반드시 n의 제곱근 이하의 숫자이기 때문에 n의 제곱근 이하까지만 비교하면 된다.
# for..else문 -> for문이 끝났을 때 아래에 있는 else부분을 출력한다.
# 그 내부에 break문이 있으면 else부분을 실행되지 않는다.
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number+1):   # 2~n까지가 n에 들어간다.
        for i in range(2, n):    # 소수들로 나누어떨어지는 지를 확인 -> 소수들은 prime_list에 있음
            if i * i <= n and n % i == 0 :    # i <= sqrt(n)보다 i * i <= n이 연산이 더 빨라서 저렇게 씀씀
                break
        else:       # 아무 숫자로도 나누어떨어지지 않았다면 / 특히 n이 2일때 위 for문은 실행되지 않는다. 이때 이 else문으로 넘어오게..
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)