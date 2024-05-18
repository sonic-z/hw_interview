class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not bool(self.stack)

    def push(self, new_element):
        self.stack.append(new_element)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)


def check(string_of_brackets):
    start_brackets = '([{'
    end_brackets = ')]}'
    new_stack = Stack()
    for s in string_of_brackets:
        if s in start_brackets:
            new_stack.push(s)
        elif s in end_brackets:
            if new_stack.is_empty() or start_brackets.index(new_stack.pop()) != end_brackets.index(s):
                return 'Несбалансированно'
    if new_stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


def main():
    tasks = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '{{[()]}}',
        '}{}',
        '{{[(])]}}',
        '[[{())}]'
    ]

    for task in tasks:
        print(check(task))


if __name__ == '__main__':
    main()
