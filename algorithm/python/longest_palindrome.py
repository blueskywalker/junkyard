import sys

class Solution:
    def isPalindrome(self, s:str) -> bool:
        if len(s) < 2:
            return False
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for start in range(len(s)-1):
            for end in range(start+1, len(s)):
                teststr = s[start:end]
                if self.isPalindrome(s[start:end]):
                    if len(teststr) > len(longest):
                        longest = teststr

        return longest


class Solution1:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # init
        table = [[ 0 for x in range(n)] for y in range(n)]

        max_length = 1
        i =0
        while i < n -1 :
            table[i][i] = True
            i = i + 1

        start = 0
        i = 0
        while i < n - 1:
            if s[i] == s[i+1]:
                table[i][i+1] = True
                start = i
                max_length = 2
            i += 1

        k = 3
        while k <= n:
            i = 0
            while i < (n - k + 1):
                j = i + k - 1

                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k
                i += 1
            k += 1

        return s[start: max_length]

s = Solution1()

test='babadad'
long=s.longestPalindrome(test)
print(long)
