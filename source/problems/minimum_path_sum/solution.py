class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        costs = [[float("inf")] * n for _ in range(m)]
        costs[0][0] = grid[0][0]
        for i in range(1, m):
            costs[i][0] = costs[i - 1][0] + grid[i][0]
        for i in range(1, n):
            costs[0][i] = costs[0][i - 1] + grid[0][i]


        for i in range(1, m):
            for j in range(1, n):
                costs[i][j] = grid[i][j] + min(costs[i - 1][j], costs[i][j - 1])
        
        return costs[-1][-1]