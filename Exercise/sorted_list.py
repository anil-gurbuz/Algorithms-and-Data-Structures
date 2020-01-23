class SortedList:
    def __init__(self):
        self.list=[]
        self.count=0

    def __len__(self):
        return len(self.list)

    def is_empty(self):
        return len(self)==0

    def add(self,item):
        index=0
        while index<len(self) and item<self.list[index]:
            index +=1

        self.list.append(0)

        for i in range(self.count,index-1,-1):
            self.list[i+1]=self.list[i]

        self.list[index]=item
        count+=1



    def delete(self,index):
        assert not self.is_empty(), 'Empty list can not delete'
        for i in range(index,len(self)-1):
            self.list[i]=self.list[i+1]


        del self.list[len(self)-1]

        self.count -=1


    def search(self,item):
        for i in self.list:
            if i==item:
                return True
            if item < i :
                break


        return False


    def index(self,item):
        for i in range(len(self)):
            if self.list[i] == item:
                return i

            elif self.list[i] > item:
                break


        return -1


    def __str__(self):
        string=''

        for i in range(len(self)):
            string += self.list[i] + ' '

        return string






