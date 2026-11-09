class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        # "00:00"
        # convert input to minutes
        minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]

        # sort times in ascending order
        minutes.sort()

        # find minimum difference across adjacent elements
        ans = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))

        # return min between currrent min and difference between last and first element
        return min(ans, 24 * 60 - minutes[-1] + minutes[0])