class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # Calculate the right sum mathematically
            right_sum = total_sum - left_sum - num
            
            # Check if left and right balances match
            if left_sum == right_sum:
                return i
            
            # Add current number to left sum for the next iteration
            left_sum += num
            
        return -1