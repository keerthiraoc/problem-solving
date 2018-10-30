class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        m = A[0]
        c = -2147483647
        for i in A:
            c = max(i, c+i)
            m = max(m, c)
        return m