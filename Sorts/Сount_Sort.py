# Алгоритм: Сортировка подсчетом (Заимствовано у Ильи)
def counting_sort(sp):
    max_item = max(sp)
    lst = [0 for _ in range(max_item + 1)]
    for i in sp:
        lst[i] = lst[i] + 1
    res_sp = []
    for i in range(len(lst)):
        if lst[i]:
            res_sp.extend([i] * lst[i])
    return res_sp