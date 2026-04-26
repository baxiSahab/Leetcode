from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int, left = 0 , right = None) -> bool:
        row,col=len(matrix), len(matrix[0])
        
        if right == None:
            right = row * col - 1
        if left>right: return False
        

        m = left + (right - left) // 2
        m_index = self.indexy(row,col,m)
        if matrix[m_index[0]][m_index[1]] == target:
            return True
        
        if target < matrix[m_index[0]][m_index[1]]:
            return self.searchMatrix(matrix , target , left = left , right = m - 1)
        else:
            return self.searchMatrix(matrix , target , left = m+1 , right=right)
        

    def indexy(self,row, col, m):
        rowy = m // col
        coly = m % col
        return [rowy,coly]

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))   # True
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False
print(s.searchMatrix([[1]], 1))                                      # True
print(s.searchMatrix([[1]], 2))                                      # False
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))  # True