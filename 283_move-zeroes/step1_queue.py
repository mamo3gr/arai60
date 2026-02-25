import collections


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        キューを利用したパターン。
        時間計算量は O(N) だが、空間計算量も O(N) で、この空間計算量は
        numsの（部分的な）コピーを取った場合と変わらない。したがって、
        in-placeな操作を求める出題意図に反していると考えられる。
        """
        zero_indices = collections.deque()
        for i, num in enumerate(nums):
            if num == 0:
                zero_indices.append(i)
                continue

            if zero_indices:
                zero_index = zero_indices.popleft()
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_indices.append(i)
