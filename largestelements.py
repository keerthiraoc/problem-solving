# class Solution:
#     # @param A : tuple of integers
#     # @return a strings
#     def largestNumber(self, A):
#         from itertools import permutations as pr
#         B=[]
#         for i in A:
#             B.append(str(i))
#         C=list(pr(B))
#         D=[]
#         for i in C:
#             Dappend("".join(map(str,i)))
#         return max(D)

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        def comp(x,y):
            sx = str(x)
            sy = str(y)
            sx += sy
            sy += sx
            if sy > sx:
                return 1
            elif sy < sx:
                return -1
            else:
                return 0
        A = sorted(A, key=functools.cmp_to_key(comp))
        if A[0] == 0:
            return "0"
        else:
            return ''.join([str(i) for i in A])