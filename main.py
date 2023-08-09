class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        v = []
        if len(s) < 3 :
            return 0

        for i in range(0, len(s) - 2) :
            if  s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i + 2] != s[i] :
                    buff = ""
                    buff += s[i]
                    buff += s[i + 1]
                    buff += s[i + 2]
                    v.append(buff)

        return len(v)