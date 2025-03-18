class Stack:
    def __init__(self):
        self.stack = list()

    def push(self,n):
        if len(self.stack) < 100:
            self.stack.append(n)
            print('ok')
        else:
            print('overflow')

    def pop(self): print(self.stack.pop() if self.stack else 'error' )

    def back(self): print( self.stack[-1] if self.stack else 'error')

    def size(self): print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print('ok')

    @staticmethod
    def exit():
        print('bye')
        exit()

    def execute(self,cmd):
        command_stack = {
            'push': self.push,
            'pop': self.pop,
            'back': self.back,
            'size': self.size,
            'clear': self.clear,
            'exit': self.exit,
        }

        operation = cmd.split()
        if not operation: return

        if command_stack.get(operation[0]):
            if len(operation) == 2 and operation[0] == 'push':
                command_stack[operation[0]](operation[1])
                return
            elif operation[0] != 'push' and len(operation) == 1:
                command_stack[operation[0]]()
                return
            else: print('error')
        else: print('error')



def action_stack():
    stack = Stack()
    while True: stack.execute(input())

action_stack()
