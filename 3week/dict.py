'''
put(key, value)
get(key) // value를 반환
'''
class LinkedTuple:
  def __init__(self):
    self.items = []

  def add(self, key, value):
    self.items.append((key, value))

  def get(self, key):
    for k, v in self.items:
      if k == key:
        return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


class Dict:
  def __init__(self):
    self.items = [None] * 8

  def put(self, key, value):
    index = hash(key) % len(self.items)
    self.items[index] = value 

  def get(self, key):
    index = hash(key) % len(self.items)
    return self.items[index]
  
my_dict =Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
print(my_dict.items)

'''
1. 체이닝 기법 - 충돌이 일어나는 값들을 링크드 리스트로 저장
self.items[1] = ["333", 7] -> ["77", 6] 
2. open addressing
'''