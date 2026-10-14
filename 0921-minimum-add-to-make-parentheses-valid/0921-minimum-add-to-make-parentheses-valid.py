class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        closing = 0

        for ch in s:
            if ch == '(':
                open += 1
            else:
                if open>0:
                    open -= 1
                else:
                    closing += 1
        return open+closing