# ==============================
# Singly Linked List
# ==============================

class Node:
    def __init__(self, value):
        self.value = value   # value stored in the node
        self.next = None     # reference to the next node


# create nodes
a = Node(5)
b = Node(8)
c = Node(12)

# link nodes together
a.next = b
b.next = c

# a -> b -> c -> None


# traverse the list
current = a

while current:
    print(current.value)
    current = current.next   # move to the next node




# ==============================
# Doubly Linked List
# ==============================

class DNode:
    def __init__(self, value):
        self.value = value   # value stored in the node
        self.next = None     # reference to the next node
        self.prev = None     # reference to the previous node


# create nodes
x = DNode(5)
y = DNode(8)
z = DNode(12)

# link nodes forward
x.next = y
y.next = z

# link nodes backward
y.prev = x
z.prev = y

# None <- x <-> y <-> z -> None


# traverse forward
current = x

while current:
    print(current.value)
    current = current.next


# traverse backward
current = z

while current:
    print(current.value)
    current = current.prev