def solution(s):
    stack = []
    for c in s:
        if (c == '('):
            stack.append(c)
        else:
            if (not stack):
                 return False
            else:
                 if (stack[-1] == '('):
                      stack.pop()
        
    if (not stack) :
        return True
    else:
        return False