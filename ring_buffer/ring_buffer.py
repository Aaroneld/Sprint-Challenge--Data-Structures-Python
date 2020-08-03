class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []
        self.oldest = None

    def append(self, item):
        if len(self.store) == 0:
            self.store.append(item)
            self.oldest = 0
        elif len(self.store) >= self.capacity:
           if self.oldest != self.capacity - 1:
               self.store.pop(self.oldest)
               self.store.insert(self.oldest, item)
               self.oldest += 1
           else: 
               self.store.pop(-1)
               self.store.append(item)
               self.oldest = 0
        else:
            self.store.append(item)


    def get(self):
        returnArr = []
        [returnArr.append(x) for x in self.store if x != None]
        return returnArr



buffer = RingBuffer(5)

buffer.append(1)
buffer.append(2)
buffer.append(3)
buffer.append(4)
buffer.append(5)
buffer.append(13)
buffer.append(15)
buffer.append(14)
buffer.append(16)
buffer.append(14)
buffer.append(16)

print(len(buffer.store))
print(buffer.get())