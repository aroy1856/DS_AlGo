def partition(arr, start, end):
    #Choose the last element of the array as the pivot element
    pivot = arr[end]
    #no of element that are less than pivot which are encountered
    i = start - 1
    
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
   
    (arr[i+1], arr[end]) = (arr[end], arr[i+1])
    
    return i+1 


def quickSort(arr, s, e):
    
    while s < e:
        p = partition(arr, s, e)
        
        quickSort(arr, s, p-1)
        quickSort(arr, p+1, e)


array = [ 10, 7, 8, 9, 1, 5 ]
quickSort(array, 0, len(array) - 1)        