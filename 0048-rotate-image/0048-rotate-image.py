class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(i + 1,cols):
                if i != j:
                    matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]

        def reverse(m):
            i = 0 
            j = len(m) - 1
            while i < j:
                m[i], m[j] = m[j], m[i]
                i += 1
                j -= 1
        
        for i in range(rows):
            reverse(matrix[i])
        
        return matrix