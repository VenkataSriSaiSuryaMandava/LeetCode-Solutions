class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = Counter(s)
        prefix = []
        
        i = 0
        while i < n and counts[target[i]] > 0:
            counts[target[i]] -= 1
            prefix.append(target[i])
            i += 1
            
        for pos in range(i, -1, -1):
            if pos < n:
                for c_code in range(ord(target[pos]) + 1, ord('z') + 1):
                    ch = chr(c_code)
                    if counts[ch] > 0:
                        counts[ch] -= 1
                        suffix = []
                        for code in range(ord('a'), ord('z') + 1):
                            c = chr(code)
                            if counts[c] > 0:
                                suffix.append(c * counts[c])
                        return "".join(prefix[:pos]) + ch + "".join(suffix)
            
            if pos > 0:
                counts[prefix.pop()] += 1
                
        return ""