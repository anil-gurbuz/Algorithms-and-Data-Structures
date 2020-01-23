class Stack:

    def __init__(self):
        self.stack=[]
        self.top=-1
        self.count=0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count==0

    def push(self,item):
        self.stack.append(item)
        self.top +=1
        self.count +=1

    def pop(self):
        assert not self.is_empty() , 'Empty stack cant be poped'
        item=self.stack[self.top]
        self.stack.remove(item)
        self.top -=1
        self.count -=1
        return item

    def peek(self):
        assert not self.is_empty() , 'Empty stack cant be peeked'
        return self.stack[self.top]


