from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        
        num_to_group = {}
        group_to_list = {}
        
        group_idx = 0
        num_to_group[sorted_nums[0]] = group_idx
        group_to_list[group_idx] = deque([sorted_nums[0]])
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - sorted_nums[i - 1] > limit:
                group_idx += 1
            
            num_to_group[sorted_nums[i]] = group_idx
            if group_idx not in group_to_list:
                group_to_list[group_idx] = deque()
            group_to_list[group_idx].append(sorted_nums[i])
            
        res = []
        for x in nums:
            grp = num_to_group[x]
            res.append(group_to_list[grp].popleft())
            
        return res