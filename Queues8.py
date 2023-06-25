class DataStream:
    def __init__(self, value, k):
        self.value = value
        self.k = k
        self.stream = []

    def consec(self, num):
        self.stream.append(num)
        if len(self.stream) < self.k:
            return False
        return self.stream[-self.k:] == [self.value] * self.k
ds = DataStream(4,3)
print(ds.consec(4))
print(ds.consec(4))
print(ds.consec(4))
print(ds.consec(3))

