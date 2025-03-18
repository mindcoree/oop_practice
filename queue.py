class Queue:
    def __init__(self): self.queue = list()

    def push(self,n):
        if len(self.queue) < 100:
            self.queue.append(n)
            print('ok')
        else:
            print('overflow')

    def pop(self): print(self.queue.pop(0) if self.queue else 'error')

    def front(self): print(self.queue[0] if self.queue else 'error')

    def size(self): print(len(self.queue))

    def clear(self):
        self.queue.clear()
        print('ok')

    @staticmethod
    def exit():
        print('bye')
        exit()

    def execute(self,cmd):
        command_queue = {
            'push':self.push,
            'pop':self.pop,
            'front':self.front,
            'size':self.size,
            'clear':self.clear,
            'exit':self.exit,
        }

        operation = cmd.split()

        if not operation: return

        if command_queue.get(operation[0]):
            if len(operation) == 2 and operation[0] == 'push':
                command_queue[operation[0]](operation[1])
                return
            elif operation[0] != "push" and len(operation) == 1:
                command_queue[operation[0]]()
                return
            else: print('error')
        else: print('error')




def action_queue():
    queue = Queue()
    while True: queue.execute(input())


action_queue()



