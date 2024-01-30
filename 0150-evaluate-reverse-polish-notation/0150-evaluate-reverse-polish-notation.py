class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                n2, n1 = stack.pop(), stack.pop()
                stack.append(n1 - n2)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                n2, n1 = stack.pop(), stack.pop()
                stack.append(int(n1/n2))
            else:
                stack.append(int(c))
        return stack[0]