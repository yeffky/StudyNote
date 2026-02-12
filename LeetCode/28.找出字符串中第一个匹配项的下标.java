/*
 * @lc app=leetcode.cn id=28 lang=java
 *
 * [28] 找出字符串中第一个匹配项的下标
 */

// @lc code=start
class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0 || haystack.length() < needle.length()) {
            return -1;
        }
        int right = 0;
        for (int i = 0; i < haystack.length(); i++) {
            if (haystack.charAt(i) == needle.charAt(right) && i + needle.length() <= haystack.length()) {
                for (int j = i; j < i + needle.length(); j++) {
                    if (haystack.charAt(j) != needle.charAt(right)) {
                        right = 0;
                        break;
                    } else {
                        right++;
                    }
                    if (right == needle.length()) {
                        return i;
                    }
                }
            }
        }
        return -1;
    }
}
// @lc code=end

