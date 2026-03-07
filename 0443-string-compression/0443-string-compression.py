class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        l = 0
        
        for r in range(len(chars)):
            if r + 1 < len(chars) and chars[r] == chars[r + 1]:
                count += 1
            else:
                chars[l] = chars[r]
                l += 1

                if count > 1:
                    for digit in str(count):
                        chars[l] = digit
                        l += 1
                
                count = 1
        
        return l