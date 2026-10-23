class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        curr_max = 0
        for i in range(len(heights)):
            height = min(heights[l], heights[r])
            width = r - l
            area =  width * height

            curr_max = max(curr_max, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return curr_max



            

