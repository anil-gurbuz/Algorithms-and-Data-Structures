def linear_search(list,target):
    for i in list:
        if i==target:
            return True

    return False




def linear_search_for_sorted(sorted_list,target):
    for i in sorted_list:
        if i==target:
            return True
        if i > target:
            return False

    return False


