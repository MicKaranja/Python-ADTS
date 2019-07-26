class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        """Checks if stack is empty
        
        Returns:
            Boolean -- True if stack is empty else false
        """
        return self.stack == []
    
    def push(self, item):
        """Adds an item to the top of the stack
        
        Arguments:
            item {int/float/iterable} -- An item to append to the stack
        """
        self.stack.append(item)
        
    def pop(self):
        """Removes the top item from the stack and returns it
        
        Returns:
            item {int/float/iterable} -- An item to remove from the stack
        Raises:
            Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.stack.pop()
    
    def peek(self):
        """Peeks into the stack. Returns the item at the top of the stack.
        
        Returns:
            item {int/float/iterable} -- the item at the top of the stack.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.stack[len(self.stack)-1]
    
    def size(self):
        """Returns the length/number of items in the stack
        
        Returns:
            item {int/float/iterable} -- the item at the top of the stack.
        """
        return len(self.stack)

# test use case
s = Stack()
while True:
    print('push <value>')
    print('pop')
    print('peek')
    print('size')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        print('Popped value: ', s.pop())
    elif operation =='peek':
        print('Top value: ', s.peek())
    elif operation =='size':
        print(s.size())
    elif operation == 'quit':
        break