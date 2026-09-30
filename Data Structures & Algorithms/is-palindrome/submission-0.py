class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        end = len(s) - 1

        for i in range(len(s)):
            e = end - i
            if s[i] != s[e]:
                print(s[i], s[e])
                return False
            
        return True