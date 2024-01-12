class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def get_column(mat, idx):
            return [row[idx] for row in mat]    
        special = 0
        for i in range(len(mat)):
            if sum(mat[i])==1:
                idx = mat[i].index(1)
                col = get_column(mat,idx)
                if sum(col) == 1:
                    special += 1
        return special