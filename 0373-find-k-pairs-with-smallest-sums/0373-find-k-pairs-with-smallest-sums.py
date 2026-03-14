class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        res = []

        for i, num in enumerate(nums1):
            heap.append([num + nums2[0], i, 0])
        heapq.heapify(heap)

        while heap and k > 0:
            cur_sum, index1, index2 = heapq.heappop(heap)
            res.append([nums1[index1], nums2[index2]])
            k -= 1

            if index2 + 1 < len(nums2):
                new_sum = nums1[index1] + nums2[index2 + 1]
                heapq.heappush(heap, [new_sum, index1, index2 + 1])
        
        return res