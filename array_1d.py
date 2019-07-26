# Implementing the array ADT using a Python List
class Array:
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self.size = size
        self.elements = [None for i in range(size)]
        
    def __repr__(self):
        return "{}".format(self.elements)
    
    def len(self):
        return self.size
    
    def shape(self):
        return (1, self.size)
    
    def get_item(self, index):
        assert index > 0 and index < self.size, "Array subscript out of range"
        return self.elements[index]
    
    def set_item(self, index, value):
        assert index > 0 and index < self.size, "Array subscript out of range"
        self.elements[index] = value
    
    def clear(self, value):
        for i in range(self.size):
            self.elements[i] = value



a= Array(5)
print(a)
print(a.len())
a.set_item(4, "last")
print(a.get_item(4))
a.clear(0)
print(a)
print(a.shape())