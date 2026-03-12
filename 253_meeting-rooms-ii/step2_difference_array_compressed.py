import itertools

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        """
        difference arrayと座標圧縮を用いたアプローチ。
        """
        max_time, intervals = self.compress_intervals(intervals)
        room_demands = [0] * max_time
        for interval in intervals:
            room_demands[interval.start] += 1
            room_demands[interval.end] -= 1

        return max(itertools.accumulate(room_demands), default=0)

    @staticmethod
    def compress_intervals(intervals: list[Interval]) -> tuple[int, list[Interval]]:
        times = []
        for interval in intervals:
            times.append(interval.start)
            times.append(interval.end)

        times.sort()
        time_to_compressed = dict()
        num_unique_times = 0
        for t in times:
            if t in time_to_compressed:
                continue
            time_to_compressed[t] = num_unique_times
            num_unique_times += 1

        compressed_intervals = [
            Interval(
                start=time_to_compressed[interval.start],
                end=time_to_compressed[interval.end],
            )
            for interval in intervals
        ]
        return num_unique_times, compressed_intervals
