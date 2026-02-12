'''
Author: yeffky
Date: 2024-04-20 08:48:48
LastEditTime: 2025-06-17 11:19:12
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        if (s.count(s[0]) == len(s)):
            
            return s
        for i in range(len(s) - 1):
            index1 = i
            index2 = i
            while s[index1] == s[index2] and index2 < len(s):
                index2 += 1
                if (index2 == len(s)):
                    break
            index2 -= 1
            while s[index1] == s[index2]:
                index1 -= 1
                index2 += 1
                if (index1 < 0 or index2 > len(s) - 1):
                    ans = s[index1 + 1: index2]
                    break
                if s[index1] != s[index2]:
                    ans = s[index1 + 1: index2]
                    break
                if (index1 <= 0 or index2 >= len(s) - 1):
                    ans = s[index1: index2 + 1]
                    break
            if (len(ans) > len(res)):
                res = ans
        return res

        # for j in range(len(s), i, -1):
        #     if s[i: j + 1] == ''.join(reversed(str(s[i: j + 1]))) and len(s[i: j + 1]) > len(res):
        #         res = s[i: j + 1]
        #     if j - i < len(res):
        #         break
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('babad'))
    print(solution.longestPalindrome('cbbd'))
    print(solution.longestPalindrome('ac'))
    print(solution.longestPalindrome('abb'))
