class Queue:

    def __init__(self):
        self.queue=[]
        self.count=0
        self.front=0
        self.rear=-1

    def __len__(self):
        return self.count

    def is_empty(self):
        return len(self)==0

    def append(self,item):
        self.queue.append(item)
        self.count +=1
        self.rear +=1

    def serve(self):
        assert not self.is_empty() , 'Empty queue cant serve'
        item=self.queue[self.front]
        self.front +=1
        self.count -=1
        return item
    