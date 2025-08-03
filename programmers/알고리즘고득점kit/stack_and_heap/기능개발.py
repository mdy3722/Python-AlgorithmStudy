# 처음 잘못 푼 풀이
# 틀린 사유 : 배포 대기 기간이 10, 3일 때 3은 10일까지 기다려야 함
#            curr 변수로 기간을 고정해야 하는데 그렇지 않아서 3과 그 다음 기간이 비교되어 버림
# import math 

# def solution(progresses, speeds):
#     deploy_period = []
#     answer = []
#     for i in range(len(progresses)):
#         deploy_period.append(math.ceil((100 - progresses[i])/speeds[i]))
  
#     count = 1
#     for i in range(0, len(deploy_period)-1):
#         if deploy_period[i] >= deploy_period[i+1]:
#             count += 1
#         else:
#             answer.append(count)
#             count = 1
#     answer.append(count)
    
#     return answer

# 해결한 풀이
import math 

def solution(progresses, speeds):
    deploy_period = []
    answer = []
    for i in range(len(progresses)):
        deploy_period.append(math.ceil((100 - progresses[i])/speeds[i]))
  
    curr = deploy_period[0]
    count = 1
    for day in deploy_period[1:]:
        if curr >= day:
            count += 1
        else:
            answer.append(count)
            curr = day
            count = 1
    answer.append(count)
    
    return answer