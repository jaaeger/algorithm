class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        result = nums[0]

        while left <= right:
            result = min(result, nums[left])
            mid = left + ((right - left) // 2)
            result = min(result, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return result

"""
class Solution:
def findMin(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while(left < right):
        mid = (left + right) // 2
        if(nums[mid] < nums[right]):
            right = mid
        else:
            left =mid + 1
    return nums[left]
"""