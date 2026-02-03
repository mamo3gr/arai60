import bisect


class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        bisect_leftを使うバージョン。
        inspired from https://github.com/naoto-iwase/leetcode/pull/25
        """

        # for example:
        #   [3,4,5,1,2] -> [false,false,false,true,true]
        min_index = bisect.bisect_left(nums, True, key=lambda n: n <= nums[-1])
        return nums[min_index]

    def findMinBisectRight(self, nums: List[int]) -> int:
        """
        bisect_rightを使うバージョン。
        inspired from
        https://discord.com/channels/1084280443945353267/1230079550923341835/1235694567085576275
        """

        # [3,4,5,1,2] -> [false,false,false,true,true]
        # [11,13,15,17] -> [false,false,false,false]
        max_index = bisect.bisect_right(nums, False, key=lambda n: n < nums[0])
        # Pythonではマイナスのインデックスでアクセスできるので、
        # if文で分岐せずに一律引いても結果は変わらないが、
        # つまりはこういうことだよ、と書いたほうが新設に感じる
        if max_index >= len(nums):
            max_index =- len(nums)
        return nums[max_index]
