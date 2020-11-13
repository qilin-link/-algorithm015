###############################
# leetcode [56] 合并区间
###############################
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        n = len(intervals)
        res = []
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, n):
            # 下一区间的左界小于等于当前区间的右界，表示有公共部分
            if intervals[i][0] < right:
                # intervals[i]右界大于当前区间的右界，表示intervals[i]不包含于当前区间，需要更新当前区间的右界
                if intervals[i][1] > right:
                    right = intervals[i][1]
            else:
                # 没有交集
                res.append([left, right])
                # 更新当前区间左界和右界，指向下一区间
                left = intervals[i][0]
                right = intervals[i][1]
        res.append([left, right])
        return res

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    s = Solution()
    print(s.merge(intervals))




