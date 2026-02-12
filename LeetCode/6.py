import numpy
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = numRows
        if r == 1 or r >= len(s):
            return s
        mat = [[] for _ in range(r)]
        t, x = 2 * r - 2, 0
        for i, ch in enumerate(s):
            mat[x].append(ch)
            x += 1 if i % t < r - 1 else -1
        res = ''
        for i in range(len(mat)):
            row = ''.join(mat[i])
            res += row
        return res
        # matrix = [['']  * 1000 for _ in range(1000)]
        # row = 0
        # column = 0
        # index = 0
        # numColumns = 0
        # res = ''
        # while index < len(s):
        #     row = 0
        #     flag = 0
        #     while row < numRows and flag == 0:
        #         if index >= len(s):
        #             break
        #         print(row, column)
        #         matrix[row][column] = s[index]
        #         row += 1
        #         index += 1
        #     flag = 1
        #     row -= 2
        #     column += 1
        #     while row > 0 and flag == 1:
        #         if index >= len(s):
        #             break
        #         matrix[row][column] = s[index]
        #         column += 1
        #         row -= 1
        #         index += 1
        #     numColumns = column
        # for i in range(numRows):
        #     for j in range(numColumns):
        #         res += matrix[i][j] 
        # return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))
            
            
            