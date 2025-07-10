input = "abcba"
# 재귀 함수 - 문제의 범위를 조금씩 좁혀나가는 것
# 예시로 문자열이 소주만병만주소이라면
# 주만병만주
# 만병만
# 병
# 이렇게 범위를 좁혀나가는 게 재귀함수의 포인트이다.
# 파이썬의 문자열 슬라이싱을 이용해라.
# string[i:n]은 string을 인덱스 i부터 n-1까지 잘라낸다.

# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n - 1 - i]:
#             return False
#     return True
def is_palindrome(string):
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    return is_palindrome(string[1:-1])

print(is_palindrome(input))