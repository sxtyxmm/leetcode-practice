## Intuition
# The provided code appears to implement the evaluation of Reverse Polish Notation (RPN) expressions using a stack. 
## The algorithm employs a stack to keep track of operands while iterating through the tokens. 
## When an operator is encountered, it performs the corresponding operation on the top two operands in the stack.

## Approach
# The algorithm initializes an empty stack and a dictionary (`operators`) that maps operators to lambda functions 
# representing their respective operations. The algorithm then iterates through the tokens, pushing operands onto 
# the stack and performing operations when operators are encountered. The final result is the only element left in
# the stack.

## Complexity
# # - Time complexity: \(O(n)\), where \(n\) is the number of tokens in the input list. The algorithm iterates through each token once, performing constant-time operations for each token.
  
# - Space complexity: \(O(n)\), where \(n\) is the number of tokens in the input list. The space required is proportional to the number of operands in the input expression.

## Code

from typing import List
from collections import defaultdict

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = defaultdict(lambda: lambda x, y: 0, {"+": lambda x, y: x + y, "-": lambda x, y: x - y,
                                                         "*": lambda x, y: x * y, "/": lambda x, y: int(x / y)})
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                operand2, operand1 = stack.pop(), stack.pop()
                stack.append(operators[token](operand1, operand2))
        return stack[0]