def partition(order, left, right):
  pivot = order[right]
  i = left - 1

  for j in range(left, right):
    if order[j] <= pivot:
        i = i + 1
        order[i], order[j] = order[j], order[i]

  (order[i + 1], order[right]) = (order[right], order[i + 1])

  return i + 1


def quick_sort(order, left, right):
  if left < right:
    pi = partition(order, left, right)

    quick_sort(order, left, pi - 1)
    quick_sort(order, pi + 1, right)


data = [3,523,45,234,652,3]
quick_sort(data)
print(data)