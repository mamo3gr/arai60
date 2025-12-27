class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = set(nums1)
        common = []
        for n in nums2:
            if n in lookup:
                common.append(n)
                lookup.remove(n)
         
            if not lookup:
                break

        return common

    def intersectionWithoutSet(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted1 = sorted(nums1)
        sorted2 = sorted(nums2)

        i, j = 0, 0
        common_numbers = []
        while i < len(sorted1) and j < len(sorted2):
            if sorted1[i] < sorted2[j]:
                i += 1
                continue
            elif sorted1[i] > sorted2[j]:
                j += 1
                continue

            common = sorted1[i]
            assert common == sorted2[j]
            common_numbers.append(common)

            while i < len(sorted1) and sorted1[i] == common:
                i += 1

            while j < len(sorted2) and sorted2[j] == common:
                j += 1

        return common_numbers
