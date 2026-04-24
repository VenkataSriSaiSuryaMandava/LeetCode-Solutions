class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        indOrder = {}

        for i, c in enumerate(order):
            indOrder[c] = i
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if indOrder[w2[j]] < indOrder[w1[j]]:
                        return False
                    break
        
        return True