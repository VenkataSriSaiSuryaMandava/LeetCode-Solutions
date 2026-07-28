class Solution:
    def smallestPalindrome(self, s: str) -> str:
        half_len = len(s) // 2

        first_half = "".join(sorted(s[ : half_len]))
        middle = s[half_len] if len(s) % 2 else ""
        last_half = first_half[ : : -1]

        return first_half + middle + last_half