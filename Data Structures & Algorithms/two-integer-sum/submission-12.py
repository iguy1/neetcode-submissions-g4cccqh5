class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapSum = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in mapSum:
                return [mapSum[diff], i]
            mapSum[num] = i
        return