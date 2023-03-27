"""creating another file for the assignment to test the circular queue"""

class Empty(Exception):
    pass

class CircularQueue:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.head.data

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        data = self.head.data
        self.size -= 1
        if self.size == 0:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        return data

    def enqueue(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head
        self.size += 1

    def rotate(self):
        if self.is_empty():
            return
        self.tail = self.head
        self.head = self.head.next

    def contains(self, data):
        if self.is_empty():
            return False
        current = self.head
        for i in range(self.size):
            if current.data == data:
                return True
            current = current.next
        return False


"""Testing the circular queue"""

cq = CircularQueue()

print("Starting Size", len(cq) )
cq.enqueue("a")
cq.enqueue("b")
cq.enqueue("c")
print("Current Size:", len(cq) )
print("Current Head:", cq.first())
cq.rotate()
print("Current Head after rotating:", cq.first())
cq.contains("e")
print ("Does the queue contain e?", cq.contains("e"))
cq.contains("a")
print ("Does the queue contain a?", cq.contains("a"))
