'''
어떤 배열이 주어졌을 때, 배열의 모든 값이 k비트 정수 범위 안에 들어가야 한다.
이때의 최소 k값을 구해라.

k비트로 표현할 수 있는 정수의 개수는 2^k개
k는 1비트부터!

범위는 두가지로 나뉨
1. 배열에 음수가 있나? 즉 부호가 있나?
    -2^(k-1) ~ 2^(k-1) - 1
2. 부호가 없는가?
    0~2^k - 1
'''

arr = [-1, 0, 2, 7]

def find_min_k(arr):
  min_val = min(arr)
  max_val = max(arr)

  k = 1

  if min_val < 0:
    while not (-2**(k-1) <= min_val and max_val <= 2**(k-1)):
      k += 1
  else:
    while not (0 <= min_val and max_val <= 2**k - 1):
            k += 1

  return k

print(find_min_k([0, 4, 2048]))