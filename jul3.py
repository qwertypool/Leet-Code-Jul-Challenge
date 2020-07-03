class Solution:
    def next_step(self, cells):
        res = [0] * 8
        for i in range(1,7):
            res[i] = int(cells[i-1] == cells[i+1])
        return res
    
    def prisonAfterNDays(self, cells, N):
        found_dic = {}
        for i in range(N):
            cells_str = str(cells)
            if cells_str in found_dic:
                loop_len = i - found_dic[cells_str]
                return self.prisonAfterNDays(cells, (N - i) % loop_len)
            else:
                found_dic[cells_str] = i 
                cells = self.next_step(cells)      
        return cells