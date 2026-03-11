import dataclasses


@dataclasses.dataclass
class Event:
    time: int
    room_demand: int

    def __lt__(self, other):
        return (self.time, self.room_demand) < (other.time, other.room_demand)


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        events = []
        for interval in intervals:
            events.append(Event(time=interval.start, room_demand=1))
            events.append(Event(time=interval.end, room_demand=-1))

        events.sort()

        total_demand = 0
        for e in events:
            total_demand += e.room_demand
            if total_demand > 1:
                return False

        return True
