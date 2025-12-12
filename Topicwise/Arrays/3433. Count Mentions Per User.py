# https://leetcode.com/problems/count-mentions-per-user/?envType=daily-question&envId=2025-12-12

from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), -ord(x[0][0])))
        users = [0] * numberOfUsers
        result = [0] * numberOfUsers

        for type, timestamp, value in events:
            timestamp = int(timestamp)
            print(type, timestamp, value, result, users)
            if type == "OFFLINE":
                users[int(value)] = timestamp + 60
            else:
                if value == "ALL":
                    for i in range(numberOfUsers):
                        result[i] += 1
                elif value == "HERE":
                    for i in range(numberOfUsers):
                        if users[i] <= timestamp:
                            result[i] += 1
                else:
                    values = list(
                        map(lambda val: int(val.lstrip("id")), value.split(" "))
                    )
                    for id in values:
                        result[id] += 1
        return result


# print(
#     Solution().countMentions(
#         numberOfUsers=2,
#         events=[
#             ["OFFLINE", "11", "0"],
#             ["MESSAGE", "10", "id1 id0"],
#             ["MESSAGE", "12", "ALL"],
#         ],
#     )
# )
print(
    Solution().countMentions(
        numberOfUsers=3,
        events=[
            ["MESSAGE", "2", "HERE"],
            ["OFFLINE", "2", "1"],
            ["OFFLINE", "1", "0"],
            ["MESSAGE", "61", "HERE"],
        ],
    )
)
