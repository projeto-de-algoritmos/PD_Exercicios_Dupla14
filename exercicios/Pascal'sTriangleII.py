class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        linha = [1] * (rowIndex + 1)  

        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                linha[i - j] += linha[i - j - 1]  

        return linha