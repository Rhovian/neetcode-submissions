class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff not in ans:
                ans[nums[i]] =  i
            else:
                return [ans[diff], i]

