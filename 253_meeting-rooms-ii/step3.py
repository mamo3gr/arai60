import collections


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        time_to_demand = collections.defaultdict(int)
        for meeting in intervals:
            time_to_demand[meeting.start] += 1
            time_to_demand[meeting.end] -= 1

        min_rooms = 0
        total_demand = 0
        for _, demand in sorted(time_to_demand.items()):
            total_demand += demand
            min_rooms = max(min_rooms, total_demand)

        return min_rooms
