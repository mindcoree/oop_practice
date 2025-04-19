class Task:
    def __init__(self,name,priority,execution_time):
        self.name = name
        self.priority = priority
        self.execution_time = execution_time

    def compare_to(self,other):
        # сравниваем сначала приоритет, потом время выполнения
        if self.priority != other.priority:
            return self.priority - other.priority
        return self.execution_time - other.execution_time


class PriorityQueue:
    def __init__(self):
        self.heap = []


    def insert(self,task):
        self.heap.append(task)
        self._sift_up(self.size() - 1)

    def _sift_up(self,index):
        parent = (index - 1) // 2

        while index > 0 and self.heap[parent].compare_to(self.heap[index]) > 0:
            self.heap[index],self.heap[parent] = self.heap[parent],self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def is_empty(self):
        return self.size() == 0

    def extract_min(self):
        if self.is_empty():
            return None

        if self.size() == 1:
            return self.heap.pop()

        min_task = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_task



    def _sift_down(self,index):
        min_index = index
        size = self.size()
        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left].compare_to(self.heap[min_index]) < 0:
                min_index = left
            if right < size and self.heap[right].compare_to(self.heap[min_index]) < 0:
                min_index = right

            if min_index == index:
                break


            self.heap[index],self.heap[min_index] = self.heap[min_index],self.heap[index]
            index = min_index




def test_priority_queue():
    pq = PriorityQueue()

    t0 = Task('T0',2,5)
    t1 = Task('T1',1,3)
    t2 = Task('T2',1,1)
    t3 = Task('T3',3,2)

    pq.insert(t0)
    pq.insert(t1)
    pq.insert(t2)
    pq.insert(t3)

    print(f"Size queue: {pq.size()}")


    while not pq.is_empty():
        task = pq.extract_min()
        print(f"Выполнение: {task.name}, Приоритет: {task.priority}, Время: {task.execution_time}")



test_priority_queue()