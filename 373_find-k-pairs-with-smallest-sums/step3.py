import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        candidates = [
            # total, index for nums1(i) and nums2(j)
            (nums1[0] + nums2[0], 0, 0)
        ]
        heapq.heapify(candidates)
        queued_indices = set((0, 0))

        def queue_if_not_visited(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return
            if (i, j) in queued_indices:
                return
            queued_indices.add((i, j))
            heapq.heappush(candidates, (nums1[i] + nums2[j], i, j))

        smallest_pairs = []
        while candidates and len(smallest_pairs) < k:
            _, i, j = heapq.heappop(candidates)
            smallest_pairs.append((nums1[i], nums2[j]))
            queue_if_not_visited(i + 1, j)
            queue_if_not_visited(i, j + 1)

        return smallest_pairs
