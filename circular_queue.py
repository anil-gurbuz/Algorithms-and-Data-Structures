#Bounded Capacity

class Queue:
    def __init__(self,size):
        self.list = [0] * size
        self.act_size = 0
        self.front_pos = 0
        self.rear_pos = len(self.list) -1

    def __len__(self):
        return self.act_size

    def is_empty(self):
        return self.act_size == 0

    def is_full(self):
        return self.act_size == len(self.list)

    def append(self,item):
        assert not self.is_full(), 'Can not append a full list'
        index= (self.rear_pos + 1) % len(self.list)
        self.list.insert(index,item)
        self.rear_pos=index
        self.act_size +=1

    def serve(self):
        assert not self.is_empty(), 'Can not serve from an empty list'
        a= self.list[self.front_pos]
        self.front_pos = (self.front_pos +1) % len(self.list)
        self.act_size -=1
        return a
