class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def bisect(a: list[int], p: int, r: int, v: int) -> int | None:
            if p > r:
                return None
            q = (p + r) // 2
            if v == a[q]:
                return q
            if v < a[q]:
                return bisect(a, p, q - 1, v)
            return bisect(a, q + 1, r, v)

        a = list(itertools.chain.from_iterable(matrix))
        return bisect(a, 0, len(a) - 1, target) is not None
