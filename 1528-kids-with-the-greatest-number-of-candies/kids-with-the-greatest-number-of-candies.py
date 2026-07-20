class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum = max(candies)
        result = []
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                result.append(True)
            else:
                result.append(False)
                
        return result
