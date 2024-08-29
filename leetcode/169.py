# Поиск элемента, который встречается больше половины раз

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache = {}

        res = nums[0]
        max_count = 0

        for num in nums:
            cache[num] = cache.get(num, 0) + 1
            if cache[num] > max_count:
                max_count = cache[num]
                res = num

        return res

    