class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxWater = 0

        while l < r:
            maxWater = max(maxWater, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]: #changing the height here will acc change value, as area is bounded by smallest height
                l += 1
            else:
                r -= 1
                
        return maxWater
