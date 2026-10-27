class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1

            stack.append(ch)

        stack = stack[:len(stack) - k]

        start = 0
        while start < len(stack) and stack[start] == '0':
            start += 1

        ans = ''.join(stack[start:])
        return ans if ans else "0"