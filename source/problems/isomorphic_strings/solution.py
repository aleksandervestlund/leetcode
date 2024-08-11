class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}
        for e1, e2 in zip(s, t):
            if e2 in t_s or e1 in s_t:
               if t_s.get(e2) != e1 or s_t.get(e1) != e2:
                    return False
            else:
                t_s[e2] = e1
                s_t[e1] = e2
        return True
