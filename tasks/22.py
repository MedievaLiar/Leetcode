class Solution:
    res = []
    def generateParenthesis(self, N: int) -> list[str]:
        def dfs(l:int, r:int, s:str, nsLeft:int):
            if nsLeft > 0:
                if l > r:
                    dfs(l, r + 1, s + ')', nsLeft)
                dfs(l + 1, r, s + '(', nsLeft - 1)
            elif l > r:
                dfs(l, r + 1, s + ')',  nsLeft)
            else:
                Solution.res.append(s)
                return

        Solution.res = []
        dfs(0, 0, '', N)
        return Solution.res
