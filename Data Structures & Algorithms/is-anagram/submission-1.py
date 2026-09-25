class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = {
            "s": {},
            "t": {}
        }

        if len(s) != len(t) or len(s) == 0:
            return False

        for i in range(len(s)):
            if s[i] in count_map["s"]:
                count_map["s"][s[i]] += 1
            else:
                count_map["s"][s[i]] = 1

            if t[i] in count_map["t"]:
                count_map["t"][t[i]] += 1
            else:
                count_map["t"][t[i]] = 1

        return count_map["s"] == count_map["t"]
        

