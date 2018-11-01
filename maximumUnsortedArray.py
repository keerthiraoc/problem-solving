class Solution:
	# @param A : list of integers
	# @return a list of integers
	def subUnsort(self, A):
        if A == sorted(A):
            return [-1]
        else:
            for i in range(len(A)-1):
                if A[i] > A[i+1]:
                    c=i
                    break
            n = len(A)-1
            while n > 0:
                if A[n] < A[n-1]:
                    d=n
                    break
                n -= 1
            max = A[c]
            min = A[c]
            for i in range(c+1,d+1):
                if A[i] > max:
                    max = A[i]
                if A[i] < min:
                    min = A[i]
            for i in range(c):
                if A[i] > min:
                    c=i
                    break
            i = len(A)-1
            while i >= d+1:
                if A[i] < max:
                    d=i
                    break
                i -= 1
            return c, d

# A=[ 4, 15, 4, 4, 15, 18, 20 ]