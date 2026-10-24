
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return

        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        limit = min(k, len(self.stack))

        for i in range(limit):
            self.stack[i] += val
