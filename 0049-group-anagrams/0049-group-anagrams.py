class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            chars = [0] * 26
            
            for ch in word:
                chars[ord(ch) - ord('a')] += 1
            
            anagrams[tuple(chars)].append(word)
        
        return list(anagrams.values())