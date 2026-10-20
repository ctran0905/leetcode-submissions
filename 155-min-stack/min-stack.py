class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # keeps track of min value as you push onto each node 

    def push(self, value: int) -> None:
        self.stack.append(value)
        
        # If min_stack is empty, then value is current minimum
        # Else, append minimum val between value and current min
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            current_min = min(value, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()