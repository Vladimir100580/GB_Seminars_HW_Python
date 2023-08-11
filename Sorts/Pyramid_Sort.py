def SortPyr(arr):
    for i in range(len(arr) // 2 - 1, -1, -1): # перегруппировка массива (куча)
        creatingBunch(arr, len(arr), i)
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]       # перенос корня в конец
        creatingBunch(arr, i, 0)              # "проваливаемся к меньшей куче"
    return arr


def creatingBunch(arr, size_bunch, index_root):     # создаем кучу
    largest = index_root          # находим наибольший элемент (корень)
    lchild = 2 * index_root + 1   # левый дочерний элемент
    rchild = 2 * index_root + 2   # правый дочерний элемент
    if lchild < size_bunch and arr[lchild] > arr[largest]: largest = lchild   # существует ли левый или
    if rchild < size_bunch and arr[rchild] > arr[largest]: largest = rchild   # правый дочерний элемент > корня
    if largest != index_root:
        arr[index_root], arr[largest] = arr[largest], arr[index_root]
        creatingBunch(arr, size_bunch, largest)

