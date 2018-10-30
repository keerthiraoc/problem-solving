class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        # C=0
        # for i in range(len(B)-1):
            # x,y=A[i],B[i]
            # Y=[(x,y), (x+1, y), (x - 1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1,y+1),(x-1,y+1), (x+1,y-1)]
            # for j in Y:
            #     if A[i+1]==j[0] and B[i+1]==j[1]:
            #         C=C+Y.index(j)
        # return C
        x = y = 0
        for i in range(1, len(A)):
            x += abs(A[i] - A[i-1])
            y += abs(B[i] - B[i-1])
            x = y = max(x,y)
        return max(x,y)