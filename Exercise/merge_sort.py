def merge_sort(list):
    n=len(list)

    if n >1:
        mid=n //2

        left=list[:mid]
        right=list[mid:]

        merge_sort(left)
        merge_sort(right)


        i=0
        j=0
        k=0

        while i<len(left) and j < len(right):
            if left[i]<=right[j]:
                list[k]=left[i]
                i+=1
            elif left[i] > right[j]:
                list[k]=right[j]
                j +=1

            k+=1


        while i<len(left):
            list[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1


a=[1,9,3,7,4,4,6]
merge_sort(a)
print(a)

