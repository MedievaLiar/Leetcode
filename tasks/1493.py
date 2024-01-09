#beats 95% (если чуть подшаманить в угоду понимаемости кода, 99% по времени)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        class LenPair: #Пара 1/0 и длина отрезка
            def __init__(self, elem, len) -> None:
                self.elem = elem #1/0
                self.len = len
        
        #будем в массиве хранить длины отрезков из 0/1
        lengths = []
        nums.append('111')
        currentlen = 0
        for i in range(len(nums) - 1):
            currentlen += 1
            if nums[i] != nums[i+1]:
                lengths.append(LenPair(nums[i], currentlen))
                currentlen = 0
        #теперь простой перебор сумм пар за линию
        lengths.append(LenPair(0, 100)) #чтобы не писать лишний условный оператор
        maxlen = 0 
        currentlen = 0
        stacksize = 0 #сколько длин мы уже сложили


        for i in range(len(lengths)):
            if lengths[i].elem == 1:
                currentlen += lengths[i].len
                stacksize += 1
                if stacksize == 2: 
                    maxlen = max(maxlen, currentlen)
                    currentlen = lengths[i].len
                    stacksize = 1
            elif lengths[i].elem == 0:
                if lengths[i].len == 1:
                    pass #тогда просто удалим этот ноль
                elif lengths[i].len >= 1:
                    maxlen = max(maxlen, currentlen)
                    currentlen = 0
                    stacksize = 0
        return maxlen if 0 in nums else maxlen - 1 #На случай что нету нулей и нам нужно убрать единицу
        
