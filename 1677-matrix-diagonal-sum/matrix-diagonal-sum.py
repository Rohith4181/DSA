class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row = len(mat)
        col = len(mat[0])
        sum = 0

        for i in range(row):
            sum += mat[i][i]
        for i in range(row):
            j = col-i-1
            if(i!= j):
                sum += mat[i][j]
        return sum 
                   
        