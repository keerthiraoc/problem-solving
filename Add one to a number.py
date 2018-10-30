def plusOne(self, A):
    X=0
    for i in range(len(A)):
        X*=10
        X=A[i]+X
    X=X+1
    Y=str(X)
    C=[]
    for i in Y:
        C.append(int(i))
    return C