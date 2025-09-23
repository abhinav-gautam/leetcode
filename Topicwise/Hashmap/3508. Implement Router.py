# https://leetcode.com/problems/implement-router/description/?envType=daily-question&envId=2025-09-20
from typing import List
import bisect


class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = []
        self.map = {}
        self.destinationMap = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.map and self.map[
            (source, destination, timestamp)
        ] == 1:
            return False
        if len(self.queue) == self.memoryLimit:
            self.forwardPacket()

        self.queue.append([source, destination, timestamp])
        self.map[(source, destination, timestamp)] = 1
        self.destinationMap.setdefault(destination, []).append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.queue) == 0:
            return []
        source, destination, timestamp = self.queue.pop(0)
        self.map[(source, destination, timestamp)] = 0
        destinationList = self.destinationMap[destination]
        timestampIndex = bisect.bisect_left(destinationList, timestamp)
        if (
            timestampIndex < len(destinationList)
            and destinationList[timestampIndex] == timestamp
        ):
            destinationList.pop(timestampIndex)
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination in self.destinationMap:
            destinationList = self.destinationMap[destination]
            startIndex = bisect.bisect_left(destinationList, startTime)
            endIndex = bisect.bisect_right(destinationList, endTime)
            return endIndex - startIndex
        return 0

    def __str__(self):
        return f"Map: {self.map} \nDestination Map: {self.destinationMap}\nQueue: {self.queue}"


router = Router(3)
router.addPacket(1, 4, 90)
router.addPacket(2, 5, 90)
router.addPacket(1, 4, 90)
router.addPacket(3, 5, 95)
router.addPacket(4, 5, 105)
router.forwardPacket()
router.addPacket(5, 2, 110)
print(router.getCount(5, 100, 110))
print(router)
