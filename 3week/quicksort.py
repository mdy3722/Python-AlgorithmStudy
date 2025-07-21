'''
퀵 정렬
1. 피벗 선택 - 배열에서 임의의 원소(보통 첫번째, 중간, 마지막 요소)를 피벗으로 정함.
2. 분할 : 피벗보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 나누는 작업을 반복
3. 재귀 정렬 : 나눠진 좌/우 배열에 대해 다시 피벗을 선택하고 같은 작업을 재귀적으로 반복

평균 시간복잡도 : O(NlogN)
최악의 경우(이미 정렬된 경우) : O(N^2)
'''

def quick_sort(arr, start, end):
  if start >= end:
        return
  
  pivot = arr[start]
  left = start + 1
  right = end
  
  while left <= right:
      while left <= right and arr[left] <= pivot:
          left += 1
      while right >= left and arr[right] >= pivot:
          right -= 1
      if left < right:
          arr[left], arr[right] = arr[right], arr[left]
  
  arr[start], arr[right] = arr[right], arr[start]

  quick_sort(arr, start, right - 1)
  quick_sort(arr, right + 1, end)


arr = [5, 3, 7, 6, 2, 9]
quick_sort(arr, 0, len(arr) - 1)
print("정렬 결과:", arr)  