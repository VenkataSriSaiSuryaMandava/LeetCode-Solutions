class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        expected_sum = n * (n + 1) // 2
        unique_sum = sum(set(nums))
        actual_sum = sum(nums)

        duplicate_num = actual_sum - unique_sum
        missing_num = expected_sum - unique_sum

        return [duplicate_num, missing_num]