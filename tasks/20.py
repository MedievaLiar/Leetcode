#beats 95%
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for gap in s:
            if gap == '(' or gap == '{' or gap == '[':
                stack.append(gap)
            else:
                if not stack:
                    return False
                match gap:
                    case ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    case '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False                        
                    case ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False #эххх можно было бы и функцию сделать, жаль это всего лишь задача на литкоде

        return False if stack else True #Если осталась незакрытая скобка
