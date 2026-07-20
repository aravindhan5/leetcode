class NumArray:

    def __init__(self, nums: List[int]):
        # Create a prefix sum array with an extra leading zero
        # prefix[i] will store the sum of nums from index 0 to i-1
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # The sum of range [left, right] is obtained by subtracting
        # the prefix sum before 'left' from the prefix sum up to 'right'
        return self.prefix[right + 1] - self.prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)