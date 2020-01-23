def insertion_sort(list):
    n=len(list)

    for ins in range(1,n):

        sorted=ins-1
        while sorted >-1:
            if list[ins]<list[sorted]:
                list[ins], list[sorted] = list[sorted] , list[ins]
                ins -=1

            sorted-=1



def insertion_sort2(list):
    n=len(list)

    for i in range(1,n):

        current_item=list[i]

        pos=i

        while pos >0 and current_item<list[pos-1]:
            list[pos]=list[pos-1]
            pos -=1


        list[pos]=current_item








