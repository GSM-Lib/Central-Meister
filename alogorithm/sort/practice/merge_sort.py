def merge_sort(order):
    if len(order) <= 1:
        return order
    return merge(merge_sort(order[:len(order)//2]),merge_sort(order[len(order)//2:]))

def merge(left,right):
    i = 0
    j = 0
    sorted_list = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    
    if i == len(left):
        sorted_list.extend(right[j:])
    elif j == len(right):
        sorted_list.extend(left[i:])
    
    return sorted_list 


