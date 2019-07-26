class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(Node):
    def __init__(self):
        self.head = None
        #self.tail = None
        self.counter = 0

    def is_empty(self):
        return self.counter == 0

    def contains(self, target):
        current_node = self.head
        while current_node is not None and current_node.data !=target:
            current_node = current_node.next
        return current_node is not None
    
    # add node to the beginning of the linked list
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head  = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.counter += 1

    def remove(self, data):
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        
        assert current_node is not None, "The item must be in the linked-list."

        # unlink the node and return the item
        self.counter -= 1

        if current_node is self.head:
            self.head = current_node.next 
        else:
            previous_node.next = current_node.next
        return current_node.data

    def size(self):
        return self.counter
    
    def top(self):
        if self.is_empty():
            raise "Stack is Empty!"
        return self.head.data
    
    # Remove and return an elemnt from the top of the stack (ie LIFO)
    def pop(self):
        if self.is_empty():
            raise "Stack is Empty!"
        data_to_pop = self.head.data
        self.head = self.head.next
        self.counter -= 1
        return data_to_pop


    def display(self):
        current_node = self.head
        while current_node is not None:
            print("{}".format(current_node.data))
            current_node = current_node.next

# test use case
s = Stack()
print(s.size(), "\n")
s.push(1)
print(s.size() ,"\n")
s.push(5)
print(s.size() ,"\n")
s.push(10)
print(s.size() ,"\n")        
s.display()
print(s.contains(1) ,"\n")
print(s.contains(1000520) , "\n")
print(s.remove(10) , "\n")
print(s.size() , "\n")        
s.display()
print(s.is_empty())
print(s.top())
print(s.pop())
s.display()
print(s.size())
s.remove(1024550)
