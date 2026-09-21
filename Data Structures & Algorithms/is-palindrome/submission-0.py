class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in range(len(s)-1,-1,-1):
            if s[i].isdigit() or s[i].isalpha():
                t+=s[i].lower()
        return t==t[::-1]