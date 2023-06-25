class FrontMiddleBack:

    def __init__(self):
        self.front = []
        self.middle = []
        self.back = []

    def pushFront(self, val):
        self.front.append(val)

    def pushMiddle(self, val):
        self.middle.append(val)

    def pushBack(self, val):
        self.back.append(val)

    def popFront(self):
        if not self.front:
            return 1
        return self.front.pop(0)

    def popMiddle(self):
        if not self.middle:
            return 1
        return self.middle.pop(0)

    def popBack(self):
        if not self.back:
            return 1
        return self.back.pop(0)

queue = FrontMiddleBack()
queue.pushFront(1)
queue.pushFront(2)
queue.pushMiddle(3)
queue.pushBack(4)


print(queue.popFront())  # 1
print(queue.popMiddle())  # 3
print(queue.popBack())  # 5
