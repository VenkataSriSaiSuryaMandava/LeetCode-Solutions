class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26
        mid_char = ""
        for ch in s:
            freq[ord(ch) - 97] += 1
        
        half_freq = [0] * 26
        for i in range(26):
            half_freq[i] = freq[i] // 2
            if freq[i] % 2 != 0:
                mid_char = chr(97 + i)
        
        total_half_len = sum(half_freq)
        
        def count_permutations(counts: list[int]) -> int:
            total = sum(counts)
            ways = 1
            for count in counts:
                if count > 0:
                    for i in range(1, count + 1):
                        ways = ways * (total - count + i) // i
                        if ways > k:
                            return k + 1
                    total -= count
            return ways
        
        if count_permutations(half_freq) < k:
            return ""
        
        left_half = []
        for _ in range(total_half_len):
            for i in range(26):
                if half_freq[i] == 0:
                    continue
                
                half_freq[i] -= 1
                ways = count_permutations(half_freq)
                
                if ways >= k:
                    left_half.append(chr(97 + i))
                    break
                else:
                    k -= ways
                    half_freq[i] += 1
        
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]