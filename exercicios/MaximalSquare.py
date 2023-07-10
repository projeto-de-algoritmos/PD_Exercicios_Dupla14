class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        linhas = len(matrix)
        colunas = len(matrix[0])
        tamanhoMax = 0
        dp = [[0] * (colunas + 1) for _ in range(linhas + 1)]

        for i in range(1, linhas + 1):
            for j in range(1, colunas + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    tamanhoMax = max(tamanhoMax, dp[i][j])

        return tamanhoMax * tamanhoMax