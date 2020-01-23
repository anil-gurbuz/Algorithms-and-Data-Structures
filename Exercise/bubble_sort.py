def bubble_sort(list):
    n=len(list)

    for i in range(n-1,0,-1):

        for j in range(i):
            if list[j]> list[j+1]:
                temp=list[j + 1]
                list[j + 1]=list[j]
                list[j]=temp



a=[1,2,2,7,3,6,13,19,17]
bubble_sort(a)
print(a)