def selection_sort(list):
    n=len(list)
    i=0

    while i < n-1:

        index_of_smallest = i
        for j in range(i+1,n):
            if list[j]<list[index_of_smallest]:
                index_of_smallest = j

        list[i],list[index_of_smallest]=list[index_of_smallest],list[i]


        i+=1



a=[1,5,3,9,17,12,12]
selection_sort(a)
print(a)