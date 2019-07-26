# storage class for holding key/value pairs
class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return "{}: {}".format(self.key, self.value)

# Implementation of Map ADT using a Python list
class Map:
    def __init__(self):
        self.entry_list = []

    def size(self):
        return len(self.entry_list)
    
    def find_position(self, key):
        for i in range(len(self.entry_list)):
            if self.entry_list[i].key == key:
                return i
        return None

    def contains(self, key):
        index = self.find_position(key)
        return index is not None
    
    def add(self, key, value):
        index = self.find_position(key)
        if index is not None:
            self.entry_list[index].value = value
            return False
        else:
            entry = MapEntry(key, value)
            self.entry_list.append(entry)
            return True
    
    def value_of(self, key):
        index = self.find_position(key)
        assert index is not None, "Invalid map key"
        return self.entry_list[index].value
    
    def remove(self, key):
        index = self.find_position(key)
        assert index is not None, "Invalid map key"
        self.entry_list.pop(index)
    
    def display(self):
        for i in range(len(self.entry_list)):
            print("{}".format(self.entry_list[i]))


m = Map()
m.add("name", "Mike")
m.add("age", "37")
print(m.contains("name"))
print(m.size())
print(m.value_of("age"))
print(m.find_position("age"))
m.add("email", "email@email.com")
print(m.size())
m.display()
