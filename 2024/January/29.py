# Intuition
## The problem involves implementing a queue using two stacks.
## The main challenge is to ensure that the elements are ordered correctly as they would be in a queue.
## The use of two stacks allows us to simulate the enqueue and dequeue operations efficiently.

# Approach
## The `MyQueue` class is implemented with two stacks (`stack1` and `stack2`). 
## The `push` operation adds elements to `stack1`, simulating enqueue.
## The `pop` and `peek` operations involve transferring elements from `stack1` to `stack2`
## if `stack2` is empty, ensuring the correct order for dequeue and peek operations.

## Complexity
# - Time complexity:
#  - Push operation: $$O(1)$$
#  - Pop operation: Amortized $$O(1)$$ (transferring elements only when `stack2` is empty)
#  - Peek operation: Amortized $$O(1)$$ (transferring elements only when `stack2` is empty)
#  - Empty operation: $$O(1)$$
  
# - Space complexity:
 # - Overall space complexity: $$O(n)$$, where n is the number of elements in the queue. This accounts for the space used by `stack1` and `stack2`. The worst-case scenario is when all elements are in `stack1` before a dequeue operation.

## Code
class MyQueue:

    def __init__(self):
        # Two stacks to simulate the queue
        self.stack1 = []  # For enqueue (push)
        self.stack2 = []  # For dequeue (pop and peek)

    def push(self, x: int) -> None:
        # Push elements onto stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Pop from stack2
        return self.stack2.pop()

    def peek(self) -> int:
        # If stack2 is empty, transfer elements from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Peek from stack2
        return self.stack2[-1]

    def empty(self) -> bool:
        # Check if both stacks are empty
        return not self.stack1 and not self.stack2