#faster than 95%
class Solution:
    res = []
    def generateParenthesis(self, N: int) -> list[str]:
        def dfs(l:int, r:int, s:str, lsLeft:int):
            if lsLeft > 0:
                if l > r:
                    dfs(l, r + 1, s + ')', lsLeft)
                dfs(l + 1, r, s + '(', lsLeft - 1)
            elif l > r:
                dfs(l, r + 1, s + ')',  lsLeft)
            else:
                Solution.res.append(s)
                return

        Solution.res = []
        dfs(0, 0, '', N)
        return Solution.res
