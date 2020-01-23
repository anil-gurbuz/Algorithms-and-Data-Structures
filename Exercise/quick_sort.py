def quick_sort(list):
    first=0
    last=len(list)-1

    quick_sort_aux(list,first,last)


def quick_sort_aux(list,first,last):
    if first < last:
        partition_point = partitioning(list, first, last)

        quick_sort_aux(list, first, partition_point - 1)

        quick_sort_aux(list, partition_point + 1, last)


def partitioning(list,first,last):
    pivot=list[first]

    left= first+1
    right=last

    complete= False


    while not complete:

        while left <= right and list[left] <= pivot:
            left +=1

        while left <= right and list[right] >= pivot:
            right -=1

        if left<= right:
            list[left] , list[right] = list[right] , list[left]

        else:
            complete=True


    list[right] , list[first] = list[first] , list[right]

    return right



