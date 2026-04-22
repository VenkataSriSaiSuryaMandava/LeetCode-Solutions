class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        res = []

        for query in queries:
            for word in dictionary:
                count = 0

                for q, w in zip(query, word):
                    if q != w:
                        count += 1
                
                if count < 3:
                    res.append(query)
                    break
        
        return res