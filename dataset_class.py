class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    def __str__(self):
        return str(self.data[:10])

    def column(self, label):
        column = []
        for count, val in enumerate(self.header):
            if label == val:
                for i in self.data:
                    column.append(i[count])
        if label not in self.header:
            return None
        return column

    def count_unique(self, label):
        unique = set(self.column(label))
        return len(unique)
