input = "011110"
# 우리가 구하고자하는 것은 뒤집는 횟수의 최소
# 일단 모두 0000거나 1111거나,,로 만들어야 함
# 0에서 1을 마주쳤을 때 뒤집는다? 전체를 0으로 만들기 위한 작업
# 1에서 0을 마주쳤을 때 뒤집는다? 전체를 1로 만들기 위한 작업
# 최종값 000 또는 111을 만들기까지의 횟수를 각각 구하고 min함수로 최솟값을 반환
# 0으로 시작? 근데 1로 만드려고 함. 그럼 1로 만드는 것의 횟수를 더해줘야..

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':        # 문자열의 맨 앞도 생각하자구요..!
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):        # i는 0부터 문자열의 길이 - 2까지.. 다음 놈이랑 비교하니까
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':        # 1로 만드는 작업
                count_to_all_one += 1
            if string[i + 1] == '1':        # 0으로 만드는 작업
                count_to_all_zero += 1

    return min(count_to_all_zero, count_to_all_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)