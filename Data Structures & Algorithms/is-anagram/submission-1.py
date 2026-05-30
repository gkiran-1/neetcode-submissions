class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l_s = list(s)
        l_t = list(t)
        if len(s) == len(t):
            for i in l_s:
                if i in l_t:
                    l_t.remove(i)
                else:
                    return False
            return True
        else:
            return False
        