class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        elif set(s) == set(t) and len(s)==len(t):
            s_c_count = {}
            for i in s:
                if i in s_c_count:
                    s_c_count[i] += 1
                else:
                    s_c_count[i] = 1
            t_c_count = {}
            for i in t:
                if i in t_c_count:
                    t_c_count[i] += 1
                else:
                    t_c_count[i] = 1
            if s_c_count == t_c_count:
                return True
            else:
                return False
        else:
            return False
