import dataclasses
import heapq


@dataclasses.dataclass
class Event:
    time: int
    room_demand: int

    def __lt__(self, other):
        return (self.time, self.room_demand) < (other.time, other.room_demand)


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        events = []
        for interval in intervals:
            heapq.heappush(events, Event(time=interval.start, room_demand=1))
            heapq.heappush(events, Event(time=interval.end, room_demand=-1))

        room_needed = 0
        while events:
            e = heapq.heappop(events)
            room_needed += e.room_demand
            if room_needed > 1:
                return False

        return True
