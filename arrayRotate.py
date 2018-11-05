class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        j=0
        b=b%len(a)
        for i in range(len(a)):
            if i+b<len(a):
                ret.append(a[i+b])
            else:
                ret.append(a[j])
                j+=1
        return ret

B = performOps(A)
for i in range(len(B)):
    for j in range(len(B[i])):
        print B[i][j],