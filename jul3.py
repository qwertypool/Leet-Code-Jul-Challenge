class Solution(object):
    def nextCell(self,cells):
        modifiedCell = [0]*8
        for i in range(1,7):
            modifiedCell[i] = 1 - cells[i-1]^cells[i+1]
        return modifiedCell

    def prisonAfterNDays(self, cells, N):
        table = {}
        
        for i in range(0,N):
            table_cell = str(cells)
            if table_cell in table:
                pos = i - table[table_cell]
                return self.prisonAfterNDays(cells,(N - i)%pos)
            else:
                table[table_cell] = i
                cells = self.nextCell(cells)
        return cells
