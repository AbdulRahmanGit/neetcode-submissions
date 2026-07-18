class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        dp = [0] *len(intervals)

        for i in range(len(intervals)):
            dp[i] = 1
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        max_overlapping = max(dp)
        return len(intervals) - max_overlapping