class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            indexes = [0] * 26

            for ch in word:
                indexes[ord(ch) - ord('a')] += 1
            
            anagrams[tuple(indexes)].append(word)
        
        return list(anagrams.values())