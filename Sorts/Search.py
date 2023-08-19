# Алгоритм: Бинарный поиск (вариант с рекурсией, на вход требуется заранее отсортированный список)
def binary_search_rec(lst, value, left, right):
    if right < left:
        return None
    middle_point = (right - left) // 2 + left
    if lst[middle_point] < value:
        return binary_search_rec(lst, value, middle_point + 1, right)
    elif lst[middle_point] > value:
        return binary_search_rec(lst, value, left, middle_point - 1)
    else:
        return middle_point


# Алгоритм: Бинарный поиск (вариант без рекурсии, на вход требуется заранее отсортированный список)
def binary_search(in_list: list, value: int):
    left = 0
    right = len(in_list) - 1
    current = (right + left) // 2
    while in_list[current] != value:
        if right < left:
            return None
        if in_list[current] < value:
            left = current + 1
        else:
            right = current - 1
        current = (right + left) // 2
    return current
