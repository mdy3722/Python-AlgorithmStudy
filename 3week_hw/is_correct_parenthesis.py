'''
못 푼 문제

가장 최근에 연 애를 닫고, 그 다음 열린 애를 닫는다.
닫는 괄호가 나오면 바로 직전에 열렸었던 괄호가 닫힘.
-> 열린 괄호가 나오면 순서대로 쌓아서 저장해놔야하는 구나!!!! -> 스택
if ( => 스택에,,,
if )면 스택 pop
stack = ["(", "("]
)가 오면 하나 pop => ["("]
'''


def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    
    if len(stack) != 0:
        return False
    else:
        return True

print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))