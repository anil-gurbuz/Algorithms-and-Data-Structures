def binary_search(list,target):
    while len(list)>0:
        mid = len(list) // 2

        if list[mid] == target:
            return True

        elif list[mid] < target:
            list = list[mid + 1:]

        elif list[mid] > target:
            list = list[:mid]

    return False




def binary_search2(list,target):
    low=0
    high=len(list)-1

    while low<=high:

        mid=(low+high)//2

        if target==list[mid]:
            return True

        elif target<list[mid]:
            high=mid-1

        elif target>list[mid]:
            low=mid+1

    return False