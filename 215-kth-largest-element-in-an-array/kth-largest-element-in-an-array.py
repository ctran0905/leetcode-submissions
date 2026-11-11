import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []

        for num in nums:
            # appends num to end of min_heap & bubbles up
            heapq.heappush(min_heap, num)

            # if heap exceeds size k, drop the smallest element
            if len(min_heap) > k:
                # removes & returns the smallest element (at index 0)
                heapq.heappop(min_heap)

        # min_heaps retains only k largest element  
        # smallest one = k-th largest overall
        return min_heap[0]
        