class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows = len(matrix)
        ncols = len(matrix[0])

        i = 0
        j = nrows - 1
        row = -1

        while i <= j:
            mid = int((i + j) / 2)

            if target >= matrix[mid][0] and target <= matrix[mid][ncols - 1]:
                row = mid
                break

            elif target > matrix[mid][ncols - 1]:
                i = mid + 1

            else:
                j = mid - 1

        if row == -1:
            return False

        a = 0
        b = ncols - 1

        while a <= b:
            _mid = int((a + b) / 2)

            if target == matrix[row][_mid]:
                return True

            elif target > matrix[row][_mid]:
                a = _mid + 1

            else:
                b = _mid - 1
