class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        if k > len(s):
            k = len(s)
        
        # Count vowels in the first window of size k
        current_vowels = sum(1 for i in range(k) if s[i] in vowels)
        max_vowels = current_vowels
        
        # Early exit optimization if maximum possible vowels are already found
        if max_vowels == k:
            return max_vowels
        
        # Slide the window across the string
        for i in range(k, len(s)):
            # Add the next character on the right
            if s[i] in vowels:
                current_vowels += 1
            # Remove the leftmost character of the previous window
            if s[i - k] in vowels:
                current_vowels -= 1
                
            # Update the maximum count found so far
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                
            # Early exit optimization inside the loop
            if max_vowels == k:
                return max_vowels
                
        return max_vowels