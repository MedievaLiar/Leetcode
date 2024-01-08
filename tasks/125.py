#beats 95%
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while(r - l > 0):
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return(False)
        return(True)
