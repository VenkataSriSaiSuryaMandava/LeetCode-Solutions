class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int
        """
        graph = defaultdict(list)

        for i, par in enumerate(parent):
            graph[par].append(i)
        
        self.res = 1

        def dfs(node):
            longest = 0
            second_longest = 0

            for child in graph[node]:
                path_length = dfs(child)

                if s[child] != s[node]:
                    if path_length > longest:
                        second_longest = longest
                        longest = path_length
                    elif path_length > second_longest:
                        second_longest = path_length
                
            self.res = max(self.res, longest + second_longest + 1)
            return longest + 1
        
        dfs(0)

        return self.res