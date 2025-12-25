import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        heap = [
            (nums1[0] + nums2[0], 0, 0),
        ]
        heapq.heapify(heap)

        visited = set((0, 0))
        smallest_pairs = []
        while heap and len(smallest_pairs) < k:
            total, i1, i2 = heapq.heappop(heap)
            smallest_pairs.append((nums1[i1], nums2[i2]))

            if i1 + 1 < len(nums1) and (i1 + 1, i2) not in visited:
                heapq.heappush(heap, (nums1[i1 + 1] + nums2[i2], i1 + 1, i2))
                visited.add((i1 + 1, i2))

            if i2 + 1 < len(nums2) and (i1, i2 + 1) not in visited:
                heapq.heappush(heap, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
                visited.add((i1, i2 + 1))

        return smallest_pairs
