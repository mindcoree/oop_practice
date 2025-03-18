class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return not self.stack


class Solution:
    def isValid(self, s: str) -> bool:
        dictionary_brackets = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = Stack()
        for bracket  in s:
            if bracket  in dictionary_brackets:
                stack.push(bracket )
            else:
                top_element = stack.pop()
                if top_element is None or dictionary_brackets.get(top_element) != bracket :
                    return False
        return stack.is_empty()


