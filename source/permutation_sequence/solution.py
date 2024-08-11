from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perms = permutations(range(1, n + 1))
        for _ in range(k):
            perm = next(perms)
        return "".join(str(i) for i in perm)
