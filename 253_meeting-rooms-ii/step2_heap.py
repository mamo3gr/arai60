import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        active_meeting_ends = []
        for meeting in intervals:
            if active_meeting_ends and active_meeting_ends[0] <= meeting.start:
                heapq.heappop(active_meeting_ends)
            heapq.heappush(active_meeting_ends, meeting.end)

        return len(active_meeting_ends)
