class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        def helper(log):
            identifier, content = log.split(" ", 1)

            if content[0].isalpha():
                return (0, content, identifier)
            else:
                return (1, )
        
        return sorted(logs, key = helper)