class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for idx, num in enumerate(nums):
            desire = target - num
            if desire in nums_dict:
                return [nums_dict[desire], idx]
            nums_dict[num] = idx
