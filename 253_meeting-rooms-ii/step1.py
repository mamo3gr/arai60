import dataclasses

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


@dataclasses.dataclass
class Event:
    time: int
    room_demand: int

    def __lt__(self, other):
        return (self.time, self.room_demand) < (other.time, other.room_demand)


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append(Event(time=interval.start, room_demand=1))
            events.append(Event(time=interval.end, room_demand=-1))

        events.sort()

        total_demand = 0
        min_rooms = 0
        for e in events:
            total_demand += e.room_demand
            if total_demand > min_rooms:
                min_rooms = total_demand

        return min_rooms
