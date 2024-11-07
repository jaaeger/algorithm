class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}
        for idx, num in enumerate(nums):
            desire = target - num
            if desire in n_dict:
                return [n_dict[desire], idx]
            n_dict[num] = idx