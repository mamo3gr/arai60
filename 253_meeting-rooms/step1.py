"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals_sorted = sorted(intervals, key=lambda x: x.start)
        for i in range(len(intervals_sorted) - 1):
            if intervals_sorted[i].end > intervals_sorted[i + 1].start:
                return False

        return True
