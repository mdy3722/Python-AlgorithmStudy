'''
문제 설명
카카오에 신입 개발자로 입사한 콘은 선배 개발자로부터 개발역량 강화를 위해 다른 개발자가 작성한 소스 코드를 분석하여 문제점을 발견하고 수정하라는 업무 과제를 받았습니다.
소스를 컴파일하여 로그를 보니 대부분 소스 코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류가 나는 것을 알게 되었습니다.
수정해야 할 소스 파일이 너무 많아서 고민하던 콘은 소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램을 다음과 같이 개발하려고 합니다.

용어의 정의
'(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면 이를 "균형잡힌 괄호 문자열"이라고 부릅니다. 
그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는 이를 "올바른 괄호 문자열"이라고 부릅니다. 
예를 들어, "(()))("와 같은 문자열은 균형잡힌 괄호 문자열 이지만 올바른 괄호 문자열은 아닙니다.
반면에 "(())()"와 같은 문자열은 균형잡힌 괄호 문자열 이면서 동시에 올바른 괄호 문자열 입니다.

'(' 와 ')' 로만 이루어진 문자열 w가 균형잡힌 괄호 문자열 이라면 다음과 같은 과정을 통해 올바른 괄호 문자열로 변환할 수 있습니다.

1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.

균형잡힌 괄호 문자열 p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 올바른 괄호 문자열로 변환한 결과를 반환하시오.

"(()())()"	# -> "(()())()"
")("        # -> "()"
"()))((()"	# -> "()(())()" => u = () v = ))((() => v_u = ))((, v_v = ()
                                                     => ( + v_v_u =() => (()) + v_u의 처음과 마지막 제거 => )( => 괄호방향 뒤집 => () => (())()     
'''

# 큐에 ( 또는 )을 집어넣고 다음 것이 다른 거라면 바로 u의 후보가 됨! pop을 진행하고 문자열 덧붙여서 u를 확정.
# 같은 것이라면 계속 append 하다가  

# 아니면 괄호 각각에 대하여 개수가 같으면 u가 됨! => 자료구조: dict = {"(" : 개수, ")": 개수} -> dict["("] == dict[")"] -> result에 추가



from collections import deque

balanced_parentheses_string = "()))((()"

queue = deque()
result = ""

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
    
def change_to_correct_parenthesis(balanced_parentheses_string):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if balanced_parentheses_string == '':
        
        return ''
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    u, v = seperate_to_u_v(balanced_parentheses_string)
    # print("u is", u, "v is", v)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
    # 4-3. ')'를 다시 붙입니다. 
    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    # 4-5. 생성된 문자열을 반환합니다.
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])
         

def seperate_to_u_v(string):
    queue = deque(string)
    left_count, right_count = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char
        if char == "(":
            left_count += 1
        if char == ")":
            right_count += 1
        
        if left_count == right_count:
            break
        
    v = ''.join(queue)     # join(): 파이썬에서 특정 리스트를 입력했을 때 그 리스트의 원소들을 합쳐서 문자열로 만들어주는 함수

    return u, v

def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == "(":
            reversed_string += ")"
        else:
            reversed_string += "("

    return reversed_string
    
    

def get_correct_parentheses(balanced_parentheses_string):
    if (is_correct_parenthesis(balanced_parentheses_string)):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)
    


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))