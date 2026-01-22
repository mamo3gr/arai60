class Solution:
    def rob(self, nums: list[int]) -> int:
        """これが個人的には一番分かりやすい"""
        if not nums:
            raise ValueError("nums must not be empty")

        if len(nums) <= 2:
            return max(nums)  # take nums[0] or nums[1]

        # the result of rob(nums[:i+1])
        total = [None] * len(nums)
        total[0] = nums[0]
        total[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            total[i] = max(
                nums[i] + total[i - 2],
                total[i - 1],
            )

        return total[-1]

    def robBranching(self, nums: list[int]) -> int:
        """メインループの中でインデックスの境界処理をするバージョン"""
        if not nums:
            raise ValueError("nums must not be empty")

        # the result of rob(nums[:i+1])
        total = [None] * len(nums)

        for i in range(len(nums)):
            # whether to take nums[i] or not
            take = nums[i] + total[i - 2] if i - 2 >= 0 else nums[i]
            dont_take = total[i - 1] if i - 1 >= 0 else 0
            total[i] = max(take, dont_take)

        return total[-1]

    def robWithSentinel(self, nums: list[int]) -> int:
        """番兵を置いてメインループを簡単にしたバージョン"""
        if not nums:
            raise ValueError("nums must not be empty")

        sentinels = [0, 0]
        total = sentinels + [None] * len(nums)

        for i, num in enumerate(nums, len(sentinels)):
            total[i] = max(
                num + total[i - 2],
                total[i - 1],
            )

        return total[-1]
