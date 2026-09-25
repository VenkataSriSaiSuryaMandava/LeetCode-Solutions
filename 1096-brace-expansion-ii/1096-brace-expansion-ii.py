class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(idx: int) -> tuple[set[str], int]:
            union_set = set()
            curr_concat = {""}

            while idx < len(expression):
                char = expression[idx]

                if char.isalpha():
                    j = idx
                    while j < len(expression) and expression[j].isalpha():
                        j += 1
                    word = expression[idx:j]
                    idx = j
                    curr_concat = {prefix + word for prefix in curr_concat}

                elif char == "{":
                    inner_set, next_idx = parse(idx + 1)
                    idx = next_idx
                    curr_concat = {
                        prefix + suffix
                        for prefix in curr_concat
                        for suffix in inner_set
                    }

                elif char == ",":
                    union_set |= curr_concat
                    curr_concat = {""}
                    idx += 1

                elif char == "}":
                    union_set |= curr_concat
                    return union_set, idx + 1

            union_set |= curr_concat
            return union_set, idx

        res, _ = parse(0)
        return sorted(res)