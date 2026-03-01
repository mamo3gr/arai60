class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        def is_descending(start: int) -> bool:
            """returns whether nums[start:] is descending order."""
            for i in range(start, len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    return False
            return True

        def find_next_index(query_i: int, start: int) -> int:
            """
            search for the number next to nums[query_i] in nums[start:],
            which number is the minimum but greater than nums[query_i].
            """
            min_difference = float("inf")
            index = -1
            base = nums[query_i]
            for i in range(start, len(nums)):
                difference = nums[i] - base
                if 0 < difference < min_difference:
                    index = i
                    min_difference = difference
            return index

        def sort_interval(first: int, last: int) -> None:
            """sort nums[first:last+1]."""
            for i in range(first, last + 1):
                for j in range(i, last + 1):
                    if nums[i] > nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]

        if is_descending(0):
            nums.sort()
            return

        for i in range(len(nums)):
            if not is_descending(i + 1):
                continue

            j = find_next_index(i, i + 1)
            nums[i], nums[j] = nums[j], nums[i]
            sort_interval(i + 1, len(nums) - 1)
            break
