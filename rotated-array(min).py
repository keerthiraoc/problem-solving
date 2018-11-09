def searchMin(A, low, high):
    if low == high:
        return A[low]
    mid = low + ((high-low)//2)

    if A[mid] < A[high]:
        return searchMin(A, low, mid)
    else:
        return searchMin(A, mid+1, high)

def findMin(A):
    return searchMin(A, 0, len(A)-1)

# part 1:
def findMin(A):
    left = 0
    right = len(A)-1
    while left < right:
        mid = (left+right)//2
        if A[left] < A[right] or A[mid] <A[left]:
            right = mid
        else:
            left = mid + 1
    return A[left]