#######################
# Leetcode 91. 解码方法
#######################
from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        # s是单字符时，0返回0，1-9返回都是1
        # s是字符串时，根据规则解码

