def insertion_sort(order):
    for i in range(1, len(order)):
        t = i
        for j in range(i-1,-1,-1):
            if order[i] >= order[j]:
                break
            else:
                t = j
        order.insert(t,order.pop(i))
    return order

