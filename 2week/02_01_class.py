class Person:
    def __init__(self, name):     # 생성자 - 객체를 만들 때 호출되는 함수
        self.name = name
        print("hihi iam created", self, self.name) # 객체 정보를 출력
    def talk(self):
        print("안녕하세요 저는 ", self.name, "입니다.")
person_1 = Person("유재석")
print(person_1.name)
person_1.talk()
person_2 = Person("박명수")

