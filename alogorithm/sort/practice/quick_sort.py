def partition(order, left, right):
  pivot = order[right]
  i = left - 1

  for j in range(left, right):
    if order[j] <= pivot:
        i = i + 1
        order[i], order[j] = order[j], order[i]

  (order[i + 1], order[right]) = (order[right], order[i + 1])

  return i + 1


def quickSort(order, left, right):
  if left < right:
    pi = partition(order, left, right)

    quickSort(order, left, pi - 1)
    quickSort(order, pi + 1, right)


