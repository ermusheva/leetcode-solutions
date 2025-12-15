"""
232. Implement Queue using Stacks
Difficulty: Easy
Topics: Array, Stack, Queue

Problem:
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty.
- All the calls to pop and peek are valid.

Time Complexity: O(1)
"""

from typing import List


class MyQueue:

    def __init__(self):
        self.stack = []
        self.rev_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if not self.rev_stack:
            while self.stack:
                self.rev_stack.append(self.stack.pop())
        return self.rev_stack.pop()
        

    def peek(self) -> int:
        if not self.rev_stack:
            while self.stack:
                self.rev_stack.append(self.stack.pop())
        return self.rev_stack[-1]
        

    def empty(self) -> bool:
        return not(bool(self.stack) or bool(self.rev_stack))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

def test_solution():
    """Test cases for MyQueue implementation"""
    
    # Test case 1 - Example 1 from problem
    print("Test 1: Example from LeetCode")
    
    commands = ["MyQueue", "push", "push", "peek", "pop", "empty"]
    args = [[], [1], [2], [], [], []]
    expected = [None, None, None, 1, 1, False]
    
    print(f"Operations: {commands}")
    print(f"Arguments:  {args}")
    print(f"Expected:   {expected}")
    
    obj = None
    result = []
    
    for i, command in enumerate(commands):
        if command == "MyQueue":
            obj = MyQueue()
            result.append(None)
        elif command == "push":
            obj.push(*args[i])
            result.append(None)
        elif command == "pop":
            result.append(obj.pop())
        elif command == "peek":
            result.append(obj.peek())
        elif command == "empty":
            result.append(obj.empty())
    
    print(f"Got:        {result}")
    assert result == expected, f"Test failed!"
    print("Test 1 passed!\n")

    # Test case 2
    print("Test 2")
    
    commands = ["MyQueue", "empty"]
    args = [[], []]
    expected = [None, True]
    
    print(f"Operations: {commands}")
    print(f"Arguments:  {args}")
    print(f"Expected:   {expected}")
    
    obj = None
    result = []
    
    for i, command in enumerate(commands):
        if command == "MyQueue":
            obj = MyQueue()
            result.append(None)
        elif command == "push":
            obj.push(*args[i])
            result.append(None)
        elif command == "pop":
            result.append(obj.pop())
        elif command == "peek":
            result.append(obj.peek())
        elif command == "empty":
            result.append(obj.empty())
    
    print(f"Got:        {result}")
    assert result == expected, "Test failed!"
    print("Test 2 passed!\n")

if __name__ == "__main__":
    test_solution()