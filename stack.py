class Stack:

    def __init__(self):
        self.stack_list = []
        self.size   = 0
        self.top_pos = -1

    def __len__(self):
        return self.size


    def is_empty(self):
        return self.size == 0


    def push(self,item):
        self.size += 1
        self.stack_list.append(item)
        self.top_pos +=1


    def pop(self):
        assert not self.is_empty() , "can't pop an empty stack"
        a= self.stack_list[self.top_pos]
        del(self.stack_list[self.top_pos])
        self.top_pos -=1
        self.size -=1
        return a


    def peek(self):
        assert not self.is_empty() , "can't peek an empty stack"
        return self.stack_list[self.top_pos]




