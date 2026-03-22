class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotateMat():
            l = 0
            r = len(mat) - 1

            while l < r:
                top = l
                bottom = r

                for i in range(r - l):
                    topleft = mat[top][l + i]
                    mat[top][l + i] = mat[bottom - i][l]
                    mat[bottom - i][l] = mat[bottom][r - i]
                    mat[bottom][r - i] = mat[top + i][r]
                    mat[top + i][r] = topleft
                
                l += 1
                r -= 1
        
        for i in range(4):
            if target == mat:
                return True
            
            rotateMat()

        return False