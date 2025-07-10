all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

'''
파이썬에서 딕셔너리에 대한 키값을 제거하는 법 -> del dict[]
'''

# 1번째 방법 : 2중 for문 -> O(N^2)
# 2번째 방법 : 정렬 -> 배열이 ㄱ,ㄴ,ㄷ 순이 됨 -> O(NlogN)
# 3번째 방법 : 해쉬 테이블 -> all_students를 돌면서 해쉬 테이블의 키값에 해당 학생들을 등록
# present_students를 돌면서 해쉬 테이블의 키값의 값을 제거
# 그리고 나서 남아있는 해쉬 테이블의 키 값에 해당하는 학생이 곧 결석한 한 놈!     
# O(N) * 1 + O(N) * 1 => O(N)       


def get_absent_student(all_array, present_array):
    dict= {}
    for student in all_array:
        dict[student] = True  # True 말고 아무 값이나 넣어도 됨. 학생 이름이 키

    for present_Student in present_array:
        del dict[present_Student]

    for key in dict.keys():
        return key    # 조회하자마자 반환
    


print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))