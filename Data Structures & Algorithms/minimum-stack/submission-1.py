class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:

        curr_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, curr_min))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        v, m = self.stack[-1]
        return v
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
