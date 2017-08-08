class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:] # Makes sure we get only the data, excluding the heading

    def __str__(self):
        return str(self.data[:10])  # Output first 10 lines of data when called or printed

    def column(self, label):
        column = []
        for count, val in enumerate(self.header):
            if label == val:
                for i in self.data:
                    column.append(i[count])  # If the given label matches one in the header
        if label not in self.header:         # this will output the whole column of data (of said label)
            return None
        return column

    def count_unique(self, label):
        unique = set(self.column(label))
        return len(unique)  # This outputs the number of unique items in a column

    def val_unique(self, label):
        unique = set(self.column(label))
        return unique  # Returns the unique items found within a column
