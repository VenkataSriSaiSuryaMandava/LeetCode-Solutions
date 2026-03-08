class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for ch in word1:
            count1[ch] += 1
        
        for ch in word2:
            count2[ch] += 1
        
        return set(count1.keys()) == set(count2.keys()) and sorted(count1.values()) == sorted(count2.values())