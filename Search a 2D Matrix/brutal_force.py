class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

#        #        1,        2,        3,        4,   ...,  n
#        #      n+1,      n+2,      n+3,      n+4,   ...,  2n
#        #     2n+1,     2n+2,     2n+3,     2n+4,   ...,  3n
#        #     3n+1,     3n+2,     3n+3,     3n+4,   ...,  4n
#        #               ...    
#        # (m-1)n+1, (m-1)n+2, (m-1)n+3, (m-1)n+4,   ...,  mn        

        # Brutal Force
        # Loop through every element
        # Check if that element is the same as target
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == target:
                    return True
        return False