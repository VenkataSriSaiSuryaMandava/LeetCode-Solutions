class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [1] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            anagrams[tuple(count)].append(word)
        
        return list(anagrams.values())