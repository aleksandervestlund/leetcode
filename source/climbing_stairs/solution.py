class Solution:
    def __init__(self) -> None:
        self.fibs = [0, 1]

    def climbStairs(self, n: int) -> int:
        def fib(n):
            if len(self.fibs) >= n:
                return self.fibs[n - 1]
            if n > 2:
                for i in range(2, n):
                    self.fibs.append(self.fibs[i - 1] + self.fibs[i - 2])
            return self.fibs[n - 1]

        return fib(n + 2)
