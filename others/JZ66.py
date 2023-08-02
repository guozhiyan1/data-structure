"""
B[0]=A[1]*A[2]*A[3]*A[4]
B[1]=A[0]*A[2]*A[3]*A[4]
B[2]=A[0]*A[1]*A[3]*A[4]
B[3]=A[0]*A[1]*A[2]*A[4]
B[4]=A[0]*A[1]*A[2]*A[3]
"""
class Solution:
    def multiply(self , A) :
        # write code here
        B=[]
        for i in range(len(A)):
            mul=1
            for j in range(len(A)):
                if j!=i:
                    mul=mul*A[j]
            B.insert(i,mul)
        return B