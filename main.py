# meeting room
import heapq

meeting = [[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]]


def minRooms(interval):
    if len(meeting) > 0:
        interval.sort()
        rooms = 1
        heap = [interval[0][1]]
        for start, end in interval[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        holding = max(rooms, len(heap))
        return holding


print(minRooms(meeting))









