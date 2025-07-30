'''
지갑 넓이 >= 지폐 넓이를 비교할 것이 아니라,
지폐의 작은 길이가 지갑의 작은 길이보다 크거나, 지폐의 큰 길이가 지갑의 큰 길이보다 클때까지 접기를 반복한다.

문제 조건 : 접는 쪽은 지폐에서 항상 큰 쪽. 절반으로 접고 만약 길이가 홀수면 소수점은 버린다.
wallet, bill 리스트가 주어짐

문제 : 지폐를 지갑에 넣을 수 있는 최소 횟수 구하기

'''
wallet = [30,15]
bill = [26,17]

def solution(wallet, bill):
    answer = 0
    while ((min(bill) > min(wallet)) or (max(bill) > max(wallet))):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        
        answer += 1

    return answer


print("정답은 1입니다. 정답 : ", solution(wallet, bill))