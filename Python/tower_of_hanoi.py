def hanoi(n,A,B,C):
    if n>0:
        print(A,B,C)
        hanoi(n-1,A,C,B)
        if A:
            C.append(A.pop())
        hanoi(n-1,B,A,C)
    
A=[1,2,3]
B=[]
C=[]
hanoi(3,A,B,C)
print(A,B,C)