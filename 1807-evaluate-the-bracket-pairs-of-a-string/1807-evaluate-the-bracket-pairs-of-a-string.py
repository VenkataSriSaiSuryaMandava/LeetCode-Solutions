class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k_map = {key: val for key, val in knowledge}

        res = []
        cur_key = []
        in_bracket = False

        for char in s:
            if char == "(":
                in_bracket = True
            elif char == ")":
                in_bracket = False
                key_str = "".join(cur_key)
                res.append(k_map.get(key_str, "?"))
                cur_key = []
            elif in_bracket:
                cur_key.append(char)
            else:
                res.append(char)

        return "".join(res)