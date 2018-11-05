class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        R = len(A); C = len(A[0]); l = 0; k = 0; b = []
        while k < R and l < C:
            for i in range(l,C):
                b.append(A[k][i])
            k += 1
            for i in range(k,R):
                b.append(A[i][C-1])
            C -= 1
            if k<R:
                for i in range(C-1,(l-1),-1):
                    b.append(A[R-1][i])
                R -= 1
            if l < C:
                for i in range(R-1,(k-1),-1):
                    b.append(A[i][l])
                l += 1
        return b
        
