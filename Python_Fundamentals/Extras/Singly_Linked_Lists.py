class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def remove_from_front(self):
        pass

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None



x = SList()
x.add_to_front("Jim")
x.add_to_front("Dwight")
print(x.val)