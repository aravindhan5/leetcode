class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Calculate the sum of the first window of size k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window across the rest of the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
                
        # Return the maximum average
        return max_sum / k