class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        # Stopping two elements short guarantees that j and k always have valid room to operate.
        for i in range(len(nums) - 2):
            # Skip duplicate values for i to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    
                    # Skip duplicates for j and k
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                        
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1  # Sum is too small, move left pointer right
                else:
                    k -= 1  # Sum is too large, move right pointer left
                    
        return ans