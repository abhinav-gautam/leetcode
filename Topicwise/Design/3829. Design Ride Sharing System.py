# https://leetcode.com/problems/design-ride-sharing-system/description/


class RideSharingSystem:

    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.active_riders = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.active_riders.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] not in self.active_riders:
            self.riders.popleft()

        if not self.riders or not self.drivers:
            return [-1, -1]

        rider = self.riders.popleft()
        driver = self.drivers.popleft()
        self.active_riders.remove(rider)

        return [driver, rider]

    def cancelRider(self, riderId: int) -> None:
        self.active_riders.discard(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)©leetcode
