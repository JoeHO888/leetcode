class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

#        #        1,        2,        3,        4,   ...,  n
#        #      n+1,      n+2,      n+3,      n+4,   ...,  2n
#        #     2n+1,     2n+2,     2n+3,     2n+4,   ...,  3n
#        #     3n+1,     3n+2,     3n+3,     3n+4,   ...,  4n
#        #               ...    
#        # (m-1)n+1, (m-1)n+2, (m-1)n+3, (m-1)n+4,   ...,  mn
#        
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m * n - 1  # m*n

        while start <= end:
            mid = (start + end) // 2
            row = mid // n
            column = mid % n
            if target == matrix[row][column]:
                return True
            elif target > matrix[row][column]:
                start = mid + 1
            else:
                end = mid - 1
        return False

