###################################
# leetcode [8] 字符串转换整数 (atoi)
###################################
class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())        # 去除两边空格
        if len(ls) == 0:
            return 0
        sign = -1 if ls[0] == '-' else 1    # 判断正副号
        if ls[0] in ['-','+']: del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            # 数字字符转ASCII码十进制数字相减得到数字本身，ret*10：得到的数字进位后与新得到的数字相加
            ret = ret * 10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret, 2**31 - 1))      # 越界判断

if __name__ == "__main__":
    str = " -91283472332"
    s = Solution()
    print(s.myAtoi(str))
