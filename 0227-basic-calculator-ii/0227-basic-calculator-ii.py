class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'

        for i in range(len(s)+1):
            ch = '+' if i == len(s) else s[i]

            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch != ' ':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop()*num)
                elif op == '/':
                    prev = stack.pop()
                    result = abs(prev) // abs(num)
                    if (prev < 0) != (num < 0):
                        result = -result
                    stack.append(result)
                
                op = ch
                num = 0
        return sum(stack)
        