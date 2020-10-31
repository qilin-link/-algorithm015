############################
# leetcode [5] 最长回文子串
############################
class Solution:
    # 中心扩展法
    def expendAroundCenter(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expendAroundCenter(s, i, i)    # 奇数个字符
            left2, right2 = self.expendAroundCenter(s, i, i + 1)    # 偶数个字符
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]

if __name__ == "__main__":
    s = 'babad'
    print(Solution().longestPalindrome(s))
