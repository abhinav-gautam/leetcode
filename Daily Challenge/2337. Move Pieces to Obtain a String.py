# https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/?envType=daily-question&envId=2024-12-05


# class Solution(object):
#     def canChange(self, start, target):
#         """
#         :type start: str
#         :type target: str
#         :rtype: bool
#         """

#         startPosition = {"L": [], "R": [], "_": []}
#         targetPosition = {"L": [], "R": [], "_": []}

#         for i in range(0, len(start)):
#             if start[i] == "L":
#                 startPosition["L"].append(i)
#             if start[i] == "R":
#                 startPosition["R"].append(i)
#             if start[i] == "_":
#                 startPosition["_"].append(i)

#         for i in range(0, len(start)):
#             if target[i] == "L":
#                 targetPosition["L"].append(i)
#             if target[i] == "R":
#                 targetPosition["R"].append(i)
#             if target[i] == "_":
#                 targetPosition["_"].append(i)
#         print("start", startPosition)
#         print("target", targetPosition)

#         # Inconsistent numbers
#         if (
#             len(startPosition["L"]) != len(targetPosition["L"])
#             or len(startPosition["R"]) != len(targetPosition["R"])
#             or len(startPosition["_"]) != len(targetPosition["_"])
#         ):
#             return False

#         if start.replace("_", "") != target.replace("_", ""):
#             return False

#         # Checking if L move is possible
#         for i in range(len(startPosition["L"])):

#             # If target position is on the right side
#             if startPosition["L"][i] < targetPosition["L"][i]:
#                 return False

#             if len(startPosition["R"]) == 0:
#                 if startPosition["L"][len(startPosition["L"]) - 1] > targetPosition[
#                     "L"
#                 ][len(targetPosition["L"]) - 1] and len(startPosition["L"]) == len(
#                     startPosition["_"]
#                 ):
#                     return True

#             # If gap between target and start is more than 1
#             elif startPosition["L"][i] - targetPosition["L"][i] > 0:
#                 for j in range(targetPosition["L"][i], startPosition["L"][i]):
#                     if start[j] == "R":
#                         return False

#         # Checking if R move is possible
#         for i in range(len(startPosition["R"]) - 1, -1, -1):
#             # If target position is on the right side
#             if startPosition["R"][i] > targetPosition["R"][i]:
#                 return False

#             if len(startPosition["L"]) == 0:
#                 if startPosition["R"][0] > targetPosition["R"][0] and len(
#                     startPosition["R"]
#                 ) == len(startPosition["_"]):
#                     return True

#             # If gap between target and start is more than 1
#             elif targetPosition["R"][i] - startPosition["R"][i] > 0:
#                 for j in range(startPosition["R"][i] + 1, targetPosition["R"][i] + 1):
#                     if start[j] == "L":
#                         print("returning false")
#                         return False

#         return True


class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """

        n = len(start) - 1
        i, j = 0, 0

        while i < n or j < n:
            while i < n and start[i] == "_":
                i += 1
            while j < n and target[j] == "_":
                j += 1

            print(i, j)
            print(start[i], target[j])
            if start[i] != target[j]:
                return False
            if start[i] == "L" and i < j:
                return False
            if start[i] == "R" and i > j:
                return False

            i += 1
            j += 1

        return True


obj = Solution()
print(obj.canChange("_L__R__R_", "L______RR"))
