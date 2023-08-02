class Solution:
    def printMatrix(self , matrix: List[List[int]]) -> List[int]:
        # write code here
        if not matrix:
            return None
        m=len(matrix)
        n=len(matrix[0])
        res=[]
        left,right,top,bottom=0,n-1,0,m-1
        while left<=right and top<=bottom:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            for i in range(top+1,bottom+1):
                res.append(matrix[i][right])
            if top != bottom:
                for i in range(left, right)[::-1]:
                    res.append(matrix[bottom][i])
            if left != right:
                for i in range(top+1, bottom)[::-1]:
                    res.append(matrix[i][left])
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        return res