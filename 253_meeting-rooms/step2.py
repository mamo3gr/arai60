import itertools


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals_sorted = sorted(intervals, key=lambda x: (x.start, x.end))
        for a, b in itertools.pairwise(intervals_sorted):
            if a.end > b.start:
                return False

        return True
