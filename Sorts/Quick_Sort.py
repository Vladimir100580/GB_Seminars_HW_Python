def SortQ(arr, startPos, endPos):
    leftPos, rightPos = startPos, endPos
    pivot = arr[round((startPos + endPos) / 2)]
    while True:
        while(arr[leftPos] < pivot): leftPos += 1
        while (arr[rightPos] > pivot): rightPos -= 1
        if leftPos <= rightPos:
            if leftPos < rightPos: arr[rightPos], arr[leftPos] = arr[leftPos], arr[rightPos]
            leftPos += 1
            rightPos -= 1
        if leftPos > rightPos: break
    if leftPos < endPos: SortQ(arr, leftPos, endPos)
    if startPos < rightPos: SortQ(arr, startPos, rightPos)
    return(arr)


