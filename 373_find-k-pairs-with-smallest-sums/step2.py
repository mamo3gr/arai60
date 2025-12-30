import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        candidates = [
            # total, index for nums1(i) and nums2(j)
            (nums1[0] + nums2[0], 0, 0),
        ]
        heapq.heapify(candidates)

        visited = set(
            (0, 0),  # i, j
        )
        smallest_pairs = []
        while candidates and len(smallest_pairs) < k:
            _, i, j = heapq.heappop(candidates)
            smallest_pairs.append((nums1[i], nums2[j]))

            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(candidates, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(candidates, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

        return smallest_pairs
