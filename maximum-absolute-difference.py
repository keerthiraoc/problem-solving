class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        max1 = max2 = -2147483647
        min1 = min2 =  2147483647
        for i,j in enumerate(A):
            max1 = max(max1, j + i)
            min1 = min(min1, j + i)
            max2 = max(max2, j - i)
            min2 = min(min2, j - i)
        return max(0, max1 - min1, max2 - min2)
