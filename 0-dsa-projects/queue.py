# ==============================
# Queue (FIFO) Implementation
# ==============================

# A queue follows the rule:
# First In, First Out (FIFO)
# The first element added is the first one removed.

# We'll build a queue using a linked list structure.


class Node:
    def __init__(self, value):
        self.value = value   # value stored in the node
        self.next = None     # pointer to the next node


class Queue:
    def __init__(self):
        self.front = None    # front of the queue (first element)
        self.rear = None     # rear of the queue (last element)

    def enqueue(self, value):
        # add an element to the end of the queue
        new_node = Node(value)

        if self.rear is None:        # queue is empty
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node    # link new node to the end
        self.rear = new_node         # update rear pointer

    def dequeue(self):
        # remove an element from the front of the queue
        if self.front is None:
            print("Queue is empty")
            return None

        removed_value = self.front.value
        self.front = self.front.next   # move front pointer forward

        if self.front is None:         # queue became empty
            self.rear = None

        return removed_value

    def peek(self):
        # look at the front element without removing it
        if self.front:
            return self.front.value
        return None

    def is_empty(self):
        return self.front is None


# ==============================
# Example Usage
# ==============================

q = Queue()

q.enqueue(10)   # queue: 10
q.enqueue(20)   # queue: 10 -> 20
q.enqueue(30)   # queue: 10 -> 20 -> 30

print(q.dequeue())  # removes 10
print(q.peek())     # shows next value (20)
print(q.is_empty()) # False