class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, value: int) -> None:
        self.st.append(value)

        if not self.minSt:
            self.minSt.append(value)
        else:
            self.minSt.append(min(value, self.minSt[-1]))

    def pop(self) -> None:
        if self.st:
            self.st.pop()
            self.minSt.pop()

    def top(self) -> int:
        if not self.st:
            return -1
        return self.st[-1]

    def getMin(self) -> int:
        if not self.minSt:
            return -1
        return self.minSt[-1]