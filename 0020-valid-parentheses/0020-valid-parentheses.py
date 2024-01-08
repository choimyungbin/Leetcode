class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')':'(', ']':'[','}':'{'}
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack or hashMap[c] != stack.pop():
                    return False
        if stack:
            return False
        return True