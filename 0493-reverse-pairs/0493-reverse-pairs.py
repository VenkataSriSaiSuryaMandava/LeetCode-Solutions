class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSortandCount(l, r):
            if l >= r:
                return 0
            
            m = (l + r) // 2

            count = mergeSortandCount(l, m) + mergeSortandCount(m + 1, r)

            i = l
            j = m + 1

            while i <= m and j <= r:
                if nums[i] > 2 * nums[j]:
                    count += m - i + 1
                    j += 1
                else:
                    i += 1
            
            temp = []
            i = l 
            j = m + 1

            while i <= m and j <= r:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            while i <= m:
                temp.append(nums[i])
                i += 1
            
            while j <= r:
                temp.append(nums[j])
                j += 1
            
            nums[l : r + 1] = temp

            return count
        
        return mergeSortandCount(0, len(nums) - 1)