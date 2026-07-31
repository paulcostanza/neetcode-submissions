class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        symMap = {
            '}':'{',
            ']':'[',
            ')':'(',
        }

        for c in s:
            if c in symMap:
                if stack and symMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)

        return False if stack else True