class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        x=0; y=0
        d = dict()
        for i in range(1, len(A)+1):
            d[i] = 0
        for i in A:
            if i in d:
                d[i]+=1
                if d[i] == 2:
                    x = i
        for i in d:
            if d[i] == 0:
                y = i
        return x,y