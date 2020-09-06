class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_tmp = set(s)
        if s_tmp == set(t):
            for i in s_tmp:
                if s.count(i) != t.count(i):
                    return False
                return True
        else:
            return False