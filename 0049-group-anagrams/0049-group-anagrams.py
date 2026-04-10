class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for ch in str:
                count[ord(ch) - ord('a')] += 1
            
            groups[tuple(count)].append(str)
        
        return list(groups.values())