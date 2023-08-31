from collections import deque
class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('aa')
        s = deque()

        charsLen = 0
        _len = 1
        sPointer = 0

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                _len += 1
            else:
                charsLen += 1
                s.append(str(chars[i - 1]))
                if _len != 1:
                    str_len = str(_len)
                    charsLen += len(str_len)
                    s += deque(str_len)

                _len = 1
                
            if s:
                chars[sPointer] = s.popleft()
                sPointer += 1

        while s:
            chars[sPointer] = s.popleft()
            sPointer += 1
        
        return charsLen