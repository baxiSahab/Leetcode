class Solution:
    def isSamebracket(self, closing, opening):
        # if opening == None:
        #     pass
        if closing == ')':
            if opening != '(':
                return False
        elif closing == ']':
            if opening != '[':
                return False
        elif closing == '}':
            if opening != '{':
                return False
        return True
            

    def isValid(self, s: str) -> bool:
        # TODO: Implement your solution here
        # Remember: 
        # 1. Push opening brackets to stack
        # 2. For closing brackets, check if top of stack matches
        # 3. At the end, stack should be empty
        if len(s) == 1:
            return False
        stack = []
        for element in s:
            if element in '}])':
                if len(stack) == 0:
                    return False
                elif self.isSamebracket(element, stack[-1]) == True:
                    stack.pop()
                elif self.isSamebracket(element, stack[-1]) == False:
                    return False
            else:
                stack.append(element)
        return len(stack) == 0  # Only True if ALL brackets matched
