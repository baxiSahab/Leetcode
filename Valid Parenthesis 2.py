class Solution:
    def isValid(self, s: str) -> bool:
        stack, n = [], len(s)
        if len(s) == 1:
            return False

        for bracket in s:
            if bracket in '}])':
                if len(stack) == 0:
                    return False
                elif self.helper_func(bracket, stack[-1]):
                    stack.pop()
                else:
                    return False          # mismatch
            else:
                stack.append(bracket)     # only append openers

        return stack == []


    def helper_func(self, closing: str, opening: str):
        if closing == ')':
            if opening == '(':
                return True
            else:
                return False
        if closing == ']':
            if opening == '[':
                return True
            else:
                return False
        if closing == '}':
            if opening == '{':
                return True
            else:
                return False