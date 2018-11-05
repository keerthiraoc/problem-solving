class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        res = 0
        bit = 1<<32
        while bit > A:
            bit >>= 2
        while bit !=0:
            if A >= res + bit:
                A -= res + bit
                res += bit <<1
            res >>= 1
            bit >>= 2
        return int(res)

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        high = A
        low = 1
        while low <= high:
            mid = (low + high) / 2
            # Check if mid = floor(sqrt(A))
            if  mid*mid <= A and (mid+1)*(mid+1) > A:
                return mid
            elif mid*mid < A:
                low = mid + 1
            else:
                high = mid - 1
        
        return 0 # If we were given 0, return 0 (this is the only way we'll get here)