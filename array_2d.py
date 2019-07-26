class Array2D:
    def __init__(self, rows, cols):
        self.rows=rows
        self.cols=cols
        self.array=[[None for _ in range(cols)] for _ in range(rows)]

    def __repr__(self):
        return "{}".format(self.array)

    def shape(self):
        return (self.rows, self.cols)

    def clear_array(self, value):
        self.array=[[value for _ in range(self.cols)] for _ in range(self.rows)]
        return self.array

    # Gets the contents of the element at position [i, j]
    def get_item(self, index_tuple):
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert row >= 0 and row < self.rows \
        and col >= 0 and col < self.cols, \
        "Array subscript out of range."
        return self.array[row][col]

    def set_item(self, index_tuple, value):
        assert len(index_tuple) == 2, "Invalid number of array subscripts."
        row = index_tuple[0]
        col = index_tuple[1]
        assert row >= 0 and row < self.rows \
        and col >= 0 and col < self.cols, \
        "Array subscript out of range."
        self.array[row][col] = value

    def num_cols(self):
        return self.cols
    
    def num_rows(self):
        return self.rows

    def clear(self, value):
        for i in range(self.rows):
            for j in range(self.cols):
                self.array[i][j] = value

a = Array2D(2, 3)
print(a.shape())
print(a)
a.set_item((0,0), 125)
a.set_item((0,1), 250)
a.set_item((0,2), 500)
print(a.get_item((0,0)))
a.clear(0)
print(a)
