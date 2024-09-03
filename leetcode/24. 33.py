# Бинарный поиск в ротированном массиве

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            middle_value = nums[mid]
            if target == middle_value:
                return mid

            if nums[left] <= middle_value:
                if target > middle_value or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < middle_value or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1