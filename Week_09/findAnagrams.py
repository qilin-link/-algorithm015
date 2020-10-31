##########################################
# leetcode [438] 找到字符串中所有字母异位词
# 滑动窗口解法
##########################################
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window = {}     # 定义窗口字符串统计字典
        needs = {}      # 定义目标字符串统计字典
        for c in p:
            needs[c] = needs.get(c, 0) + 1      # 统计目标字符串各字符个数，用于与窗口字符串统计结果比较
        left, right = 0, 0  # 定义左右指针
        while right < len(s):
            c = s[right]    # 将要在窗口中统计的字符
            if c not in p:
                window.clear()      # 统计的字符不匹配，则清空之前的统计结果
                left = right = right + 1   # 移除无效字符，指针右移
            else:
                window[c] = window.get(c, 0) + 1    # 匹配到字符，统计其个数
                if right - left + 1 == len(p):      # 窗口匹配字符串长度等于目标字符串长度时
                    if window == needs:             
                        res.append(left)
                    window[s[left]] -= 1            #  窗口左侧字符移除
                    left += 1                       # 左指针右移一位
                right += 1
        return res
        
if __name__ == "__main__":
    s = "cbaebabacd" 
    p = "abc"
    print(Solution().findAnagrams(s,p))
