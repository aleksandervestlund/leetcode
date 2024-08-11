class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        for i in (2, 3, 5):
            while True:
                new, rem = divmod(n, i)

                if rem != 0:
                    break

                n = new

        return n == 1
