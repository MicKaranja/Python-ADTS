# Implementation of the Set ADT container using a Python list.
class Set:
    # Creates an empty set instance.
    def __init__(self):
        self.set_elements = list()

    # Returns the number of items in the set.
    def size(self):
        return len(self.set_elements)

    # Determines if an element is in the set.
    def contains(self, element):
        return element in self.set_elements

    # Adds a new unique element to the set.
    def add(self, element):
        if element not in self.set_elements:
            self.set_elements.append(element)

    # Removes an element from the set.
    def remove(self, element):
        assert element in self.set_elements, "The element must be in the set."
        self.set_elements.remove(element)

    # Determines if two sets are equal.
    def are_equal(self, setB):
        if len(self.set_elements) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # Determines if this set is a subset of setB.
    def isSubsetOf(self, setB ):
        for element in self.set_elements:
            if element not in setB:
                return False
        return True

    # Creates a new set from the union of this set and setB.
    def union(self, setB):
        new_set = Set()
        new_set.set_elements.extend(self.set_elements)
        for element in setB:
            if element not in self.set_elements:
                new_set.set_elements.append(element)
        return new_set

    # Creates a new set from the intersection: self set and setB.
    def interset(self, setB):
        common_elements = [el for el in self.set_elements if el in setB]
        return common_elements

    # Creates a new set from the difference: self set and setB.
    def difference(self, setB):
        pass
    
    def unique(self, setB):
        unique_set=[el for el in self.set_elements if el not in setB]
        unique_set.extend([el for el in setB if el not in self.set_elements])
        return unique_set    

s = Set()
s.set_elements = [4, 5, 6]
print(s.size())
print(s.are_equal([4,5,6]))
print(s.contains(6))
print(s.isSubsetOf([1, 2, 3, 4, 5, 6, 7]))
print(s.unique([1, 2, 3, 4, 5, 6, 7]))