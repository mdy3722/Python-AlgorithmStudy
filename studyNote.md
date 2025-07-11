### 알파벳 별로 빈도수를 리스트에 저장할 때 효율적인 자료구조는 **배열**
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