'''
[⭐⭐⭐ 어려웠다...]

1. 두 사람이 선물 주고 받은 기록 있다? 이번달까지 두 사람 사이에 더 많은 선물 준 사람이 다음 달에 선물 하나 받음
2. 두 사람이 선물을 주고받은 기록이 x거나 주고받은 수가 같다? 선물지수가 더 큰 사람이 더 작은 사람에게 선물을 받음
 => 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수 - 받은 선물의 수
 => 예를 들어 A가 친구들에게 준 선물이 3개고 받은 선물이 10개라면 A의 선물 지수는 -7
 => B가 친구들에게 준 선물이 3개고 받은 선물이 2개라면 B의 선물 지수는 1
 => 만약 A와 B가 선물을 주고받은 적이 없거나 정확히 같은 수로 선물을 주고받았다면, 다음 달엔 B가 A에게 선물을 하나 받는다.
3. 선물지수도 같다면 다음 달에 선물을 주고받지 않습니다.

구하고 싶은 것 : 다음 달에 선물을 주고받을 때, 선물을 가장 많이 받을 친구가 받을 선물의 수
gifts = ["A B"]   # A가 선물을 준 친구, B가 선물을 받은 친구
테이블을 만든다. => 이차원 배열... [[0, 0, 0, ...], [], [], ...]
무지 -> 프로도
무지 -> 프로도
라이언 -> 무지
라이언 -> 무지
라이언 -> 무지
포르도 -> 무지
포르도 -> 라이언
네오 -> 무지
       무지 라이언 포르도 네오
무지    0     0     2     0
라이언  3     0     0     0
포르도  1     1     0     0
네오    1     0     0     0

배열 = [[0,0,2,0], [3,0,0,0], [1,1,0,0], [1,0,0,0]] => 이때 배열[무지] = [0,0,2,0]
=> 이를 위해서 friends가 인덱스로 표현 되어야 함
dict로 키-값 처리 => {"무지" : 0, "라이언" : 1, "포르도" : 2, "네오" : 3}

'''

friends = ["muzi", "ryan", "frodo", "neo"]

# for g in gifts: => giver, receiver = g.split() <- 이 전략을 써보자.
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]


def solution(friends, gifts):
    n = len(friends)
    name_to_idx = {name: i for i, name in enumerate(friends)}
    
    # 2차원 선물 테이블
    gift_table = [[0] * n for _ in range(n)]
    send_count = [0] * n
    recv_count = [0] * n

    # 선물 기록 파싱
    for g in gifts:
        giver, receiver = g.split()
        gi = name_to_idx[giver]
        ri = name_to_idx[receiver]
        gift_table[gi][ri] += 1
        send_count[gi] += 1
        recv_count[ri] += 1

    # 선물 지수 계산
    gift_score = [send_count[i] - recv_count[i] for i in range(n)]

    # 다음 달에 받을 선물 수
    result = [0] * n

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            give = gift_table[i][j]
            take = gift_table[j][i]
            if give > take:
                result[i] += 1
            elif give == take:
                if gift_score[i] > gift_score[j]:
                    result[i] += 1

    return max(result)

print("정답은 2입니다. 정답 : ", solution(friends, gifts))