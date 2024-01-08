class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        class StrPair: # структура чтобы со строкой хранить ее хэш
            def __init__(self, str = 100, strhash = 'asds'):
                self.str = str
                self.strhash = strhash

        #O(NMlogM), N < 10^5, M < 100, beats 80%
            
        #отсортируем каждый элемент в массиве, сохранив предыдущий в виде структуры StrPair
        for i in range(len(strs)):
            str = strs[i]
            hashed_str = hash(''.join(sorted(list(str))))
            strs[i] = StrPair(str, hashed_str)
            
        #отсортируем массив по хэшу каждой отсортированной строки
        strs = sorted(strs, key = lambda a: hash(a.strhash))
	    
        #подряд идущие будут анаграммами. выведем результат
        strs.append(StrPair())
        res = []
        anagram_list = []
        for i in range(len(strs) - 1):
            anagram_list.append(strs[i].str)
            if strs[i].strhash != strs[i+1].strhash:
                res.append(anagram_list)
                anagram_list = []
        return res
