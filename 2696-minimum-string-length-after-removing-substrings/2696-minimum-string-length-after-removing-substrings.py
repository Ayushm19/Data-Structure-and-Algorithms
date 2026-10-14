class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for ch in s:
            if stack:
                last = stack[-1]
                if (last == 'A' and ch == 'B') or (last == 'C' and ch == 'D'):
                    stack.pop()
                    continue

            stack.append(ch)
        return len(stack)