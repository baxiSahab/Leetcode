class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        new_min = min(min(self.stack ), val)
        self.min_stack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

def test_min_stack():
    ms = MinStack()
    ms.push(5)
    assert ms.getMin() == 5
    assert ms.top() == 5

    ms.push(3)
    ms.push(7)
    assert ms.getMin() == 3   # 3 is still min

    ms.pop()                  # removes 7
    assert ms.getMin() == 3   # still 3

    ms.pop()                  # removes 3
    assert ms.getMin() == 5   # min reverts to 5

    ms.push(1)
    assert ms.getMin() == 1   # new min
    print("All tests passed!")

test_min_stack()