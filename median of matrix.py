class Solution:

    def calc_se(self, A, x):
        from bisect import bisect_left, bisect_right
        smaller = equal = 0

        for row in A:
            l, r = bisect_left(row, x), bisect_right(row, x)
            smaller += l
            equal += r - l

        return smaller, equal

    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        n, m = len(A), len(A[0])
        k = (n * m + 1) // 2

        l, r = min([row[0] for row in A]), max([row[-1] for row in A])


        while l <= r:
            mid = (l + r) >> 1

            smaller, equal = self.calc_se(A, mid)

            if smaller < k and smaller + equal >= k:
                return mid
            elif smaller >= k:
                r = mid - 1
            else:
                l = mid + 1

        return -1
