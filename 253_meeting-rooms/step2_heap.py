import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


def interval_lt(self, other) -> bool:
    return (self.start, self.end) < (other.start, other.end)


Interval.__lt__ = interval_lt


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        if not intervals:
            return True

        intervals = intervals.copy()  # avoid destroying passed array
        heapq.heapify(intervals)

        for i in intervals:
            print(i.start, i.end)

        last_end = intervals[0].end
        heapq.heappop(intervals)
        while intervals:
            interval = heapq.heappop(intervals)
            if interval.start < last_end:
                return False
            last_end = interval.end

        return True
