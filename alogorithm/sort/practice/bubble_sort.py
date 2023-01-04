def bubble_sort(order):
    for i in range(len(order)):
        for j in range(len(order)-i-1):
            if order[j] <= order[j+1]:
                continue
            else:
                order[j], order[j+1] = order[j+1], order[j]

    return order
