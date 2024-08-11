class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows < 3:
            return [[1] * i for i in range(1, numRows + 1)]
        pascal = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1, 1]
            for i in range(len(pascal[-1]) - 1):
                row.insert(1, sum(pascal[-1][i : i + 2]))
            pascal.append(row)
        return pascal
