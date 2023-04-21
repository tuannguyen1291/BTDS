class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return value

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' '.join(values)

def print_queue(queue):
    if queue.is_empty():
        return
    else:
        print(queue.dequeue())
        print_queue(queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print_queue(q) # In ra màn hình các giá trị 1, 2, 3
