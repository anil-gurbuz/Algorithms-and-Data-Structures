class List:
    def __init__(self):
        self.list=[]
        self.count=0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def add(self,item):
        self.list.append(item)
        self.count +=1

    def insert(self,index,item):
        i=0
        self.list.append(0)
        while i < self.count - index  :
            self.list[self.count - i]= self.list[self.count - i -1]
            i +=1
        self.list[index]=item
        self.count +=1

    def remove(self,item):
        assert not self.is_empty(), 'Can not remove from an empty list'
        a=False
        for i in range(len(self)):
            if self.list[i]== item:
                index=i
                a = True
                break

        if a== True:
            while index < len(self) - 1:
                self.list[index] = self.list[index + 1]
                index += 1

            del (self.list[len(self) - 1])
            self.count -= 1
        else:
            print('There is not such an item in the list')



    def delete(self,index):
        assert not self.is_empty(), "Can't delete from an empty list."
        assert not index>= len(self), "Invalid Index"

        for i in range(index,len(self)-1):
            self.list[i]=self.list[i+1]

        del(self.list[len(self)-1])
        self.count -=1


    def search(self,item):
        for i in range(len(self)):
            if self.list[i]==item:
                return True

        return False


    def index(self,item):
        for i in range(len(self)):
            if self.list[i]== item:
                return i

        return -1

    def __str__(self):
        string=""
        for i in range(len(self)):
            string += (self.list[i] + ' ')
        return string

    def __getitem__(self,index):
        assert index>=0 and index< len(self), 'index out of range'
        return self.list[index]

    def __setitem__(self,index,value):
        assert index>=0 and index<len(self), 'index out of range'
        self.list[index]= value

    def __contains__(self, item):
        for i in range(len(self)):
            if self.list[i]== item:
                return True

        return False