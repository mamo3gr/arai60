class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        """
        two-pointersアプローチ。
        """
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        e = 0
        num_rooms = 0
        min_rooms = 0
        for start in starts:
            num_rooms += 1

            while e < len(ends) and ends[e] <= start:
                e += 1
                num_rooms -= 1

            min_rooms = max(min_rooms, num_rooms)

        return min_rooms
