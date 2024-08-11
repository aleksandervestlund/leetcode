from itertools import takewhile


def bisect(a: list[int], p: int, r: int, v: int) -> int | None:
    if p > r:
        return False
    q = (p + r) // 2
    if v == a[q]:
        return True
    if v < a[q]:
        return bisect(a, p, q - 1, v)
    return bisect(a, q + 1, r, v)


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n = len(matrix[0])
        return any(
            bisect(row, 0, n - 1, target)
            for row in takewhile(lambda x: x[0] <= target, matrix)
        )
