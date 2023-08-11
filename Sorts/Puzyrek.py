
def Puzyr(arr):
    l = len(arr)
    for i in range(l):
        for k in range(0, l-1-i):
            if arr[k] > arr[k+1]: arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr

