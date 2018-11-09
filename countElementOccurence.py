def findCount(A, B):
    low,high,ans = 0,len(A)-1,0
    while low <= high:
        mid = (low + high)//2
        if A[mid] == B:
            ans+=1
            high1 = mid -1
            while high1 >= low and A[high1] == B:
                ans+=1
                high1-=1
            low1 = mid+1
            while high >= low1 and A[low1] == B:
                ans+=1
                low1+=1
            break
        elif A[mid]<B:
            low = mid + 1
        else:
            high = mid - 1
    return ans