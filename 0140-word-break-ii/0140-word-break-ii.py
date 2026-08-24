class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        cache = {}

        def backtrack(i):
            if i == len(s):
                return [""]
            
            if i in cache:
                return cache[i]
            
            res = []
            for j in range(i, len(s)):
                word = s[i : j + 1]
                
                if word not in wordDict:
                    continue
                
                string = backtrack(j + 1)

                if not string:
                    continue
                
                for substring in string:
                    sentence = word
                    
                    if substring:
                        sentence += " " + substring

                    res.append(sentence)
            
            cache[i] = res
            return res
        
        return backtrack(0)