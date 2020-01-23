class CirQueue:
    def __init__(self,size):
        self.queue=[0]*size
        self.front=0
        self.rear=size-1
        self.count=0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count==0

    def is_full(self):
        return self.count==len(self.queue)

    def append(self,item):
        assert not self.is_full() , 'Cant append to a full queue'
        self.queue[(self.rear+1)%len(self.queue)]=item
        self.rear=(self.rear+1)%len(self.queue)
        self.count +=1

    def serve(self):
        assert not self.is_empty() , "Empty Stack cant serve"
        item=self.queue[self.front]
        self.front= (self.front+1)%len(self.queue)
        self.count -=1
        return item
    