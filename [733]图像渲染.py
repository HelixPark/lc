
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m, n = len(image), len(image[0])

        origColor = image[sr][sc]


        if origColor == newColor:
            return image

        def dfs(r,c):
            if image[r][c] == origColor:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1,c)  # 左

                if r+1 < m:
                    dfs(r+1,c)    # 右

                if c >= 1:
                    dfs(r,c-1)  # 上

                if c+1 < n:
                    dfs(r,c+1)  # 下

        dfs(sr,sc)
        return image
