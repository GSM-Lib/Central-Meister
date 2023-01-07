def heap_sort(order):
    lastIdx = len(order)-1
    if lastIdx < 1:
        return 

    parentIdx = get_parent(lastIdx)


    for i in range(parentIdx,-1,-1):
        heapify(order, i, lastIdx)
        
        

    for i in range(lastIdx, 0, -1):
        order[i], order[0] = order[0], order[i]
        heapify(order, 0, i-1)

def get_parent(child):
    return (child - 1) // 2

def heapify(order, parentIdx, lastIdx):
    while parentIdx * 2 + 1 <= lastIdx:
        leftChildIdx = 2 * parentIdx + 1
        rightChildIdx = 2 * parentIdx + 2
        flag = parentIdx
        
        if order[parentIdx] < order[leftChildIdx]:
            flag = leftChildIdx
            
        if rightChildIdx <= lastIdx and order[flag] < order[rightChildIdx]:
            flag = rightChildIdx
            

        if flag != parentIdx:
            order[parentIdx], order[flag] = order[flag], order[parentIdx]
            parentIdx = flag
        else:
            return

data = [213,5,125,126,2,123,1231,1,9999]
# data = [9,4,7,8,3,6,10,2,11]
heap_sort(data)
print(data)