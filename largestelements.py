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