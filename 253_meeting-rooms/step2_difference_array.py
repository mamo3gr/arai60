import itertools


class Solution:
    MAX_TIME = 1_000_000

    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        room_demands = [0] * self.MAX_TIME
        for interval in intervals:
            room_demands[interval.start] += 1
            room_demands[interval.end] -= 1

        return all(
            total_demand <= 1 for total_demand in itertools.accumulate(room_demands)
        )
