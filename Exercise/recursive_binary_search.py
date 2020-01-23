def rec_binary_search(list,target):
    n=len(list)

    if n == 0:
        return False

    mid = n // 2

    if list[mid]==target:
        return True

    if list[mid] < target :
        return rec_binary_search(list[mid+1:],target)

    if list[mid] > target:
        return rec_binary_search(list[:mid],target)





print(rec_binary_search([1,2,4,6,9,17],0))