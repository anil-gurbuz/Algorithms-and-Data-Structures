class List:
    def __init__(self):
        self.list=[]
        self.count=0

    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count==0

    def add(self,item):
        self.list.append(item)
        self.count +=1

    def insert(self,index,item):
        assert not index>= len(self) , 'Index out of range'
        assert not index < 0 , 'Index cant be smaller than zero'
        assert type(index)== int , 'Index must be an integer'

        self.list.append(0)

        for i in range(self.count,index,-1):
            self.list[i]=self.list[i-1]

        self.list[index]=item
        self.count +=1


    def remove(self,item):
        Found=False
        for i in range(len(self)):
            if self.list[i]==item:
                del self.list[i]
                self.count-=1
                found=True
                break

        if found==False:
            print('Item is not in the list')


    def delete(self,index):
        assert not index >= self.count, 'Out of range'
        assert not index < 0, 'smaller than zero'
        assert type(index) == int, 'Index must be an integer'

        for i in range(index,0,-1):
            self.list[i]=self.list[i-1]

        del self.list[0]
        self.count-=1


    def search(self,item):
        for i in range(self.count):
            if self.list[i]==item:
                return True

        return False

    def index(self,item):
        for i in range(self.count):
            if self.list[i]==item:
                return i

        return 'No such an item'


    def __getitem__(self, index):
        assert not index>=self.count , 'Out of range'
        assert not index<0, 'smaller than zero'
        assert type(index) == int, 'Index must be an integer'

        return self.list[index]

    def __setitem__(self,index,value):
        assert not index >= self.count, 'Out of range'
        assert not index < 0, 'smaller than zero'
        assert type(index) == int, 'Index must be an integer'

        self.list[index]=value

    






