### 알파벳 별로 빈도수를 리스트에 저장할 때 효율적인 자료구조는 배열
- 인덱스 0번째: a의 빈도수, 인덱스 1번째: b의 빈도수
- 문자를 아스키 코드로 변형하는 법은 ord('문자')로.. 예시: ord('a') = 97, ord('A') = 65, 반대로 chr(97) = a
- "d를 빈도수 배열에 담고 싶다?" 몇번째 인덱스로..? ord('d')-ord('a') = 3, 즉 3번째 인덱스 값은 d의 빈도수
- 이것을 일반화시키면 ord(문자) - ord('a') = index, chr(ord('a') + index) = 문자

### 코딩테스트에서 큐 사용 - collections.deque
```python
from collections import deque
queue = deque()
queue.append(3)
queue.popleft()
```

### N의 길이 배열에 대해 더하거나 뺀 모든 경우의 수 구하기
포인트는 N-1의 길이의 배열에서 **마지막 요소**를 더하거나 뺀 경우의 수를 추가하면 된다. 즉 재귀함수를 떠올릴 수 있다.
```python
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    all_ways = []

    # 모든 경우의 수
    def get_all_ways_by_doing_plus_or_minus(array, current_index, current_sum):
      if current_index == len(array):
        all_ways.append(current_sum)
        return all_ways

      get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index])
      get_all_ways_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index]) 

    return get_all_ways_by_doing_plus_or_minus(array, 0, 0)
```

### set()을 활용해 정렬과 중복 제거를 한 번에 하는 방법도 있음
예시: menus_set = set(menus)   # 정렬 + 중복 제거 -> O(N)

### Python 역순 반복
```python
for i in range(len(heights)-1, -1, -1):
```
- len(heights) - 1: 리스트 heights의 마지막 인덱스
- -1: 종료 조건 → 인덱스 0까지 포함하고 싶다면 -1로 설정
- -1: 스텝 값 → 한 번에 1씩 감소

### 내림차순 정렬
```python
array = [1,2,5,3,11]
array.sort(reverse=True)
```
### 람다를 활용한 특정 요소에 대한 정렬
```python
genre_total_play_dict = {"힙합": 1, "발라드": 10}
sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)   # item[0]이면 "장르"로 정렬, item[1]이라서 play(int)로 정렬
print(sorted_genre_play_array)    # {"발라드": 10, "힙합": 1}
```