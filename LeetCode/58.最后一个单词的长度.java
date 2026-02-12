/*
 * @lc app=leetcode.cn id=58 lang=java
 *
 * [58] 最后一个单词的长度
 */

// @lc code=start
class Solution {
    public int lengthOfLastWord(String s) {
        int len = s.length();
        int end = len - 1;
        int ans = 0;
        while (end >= 0 && s.charAt(end) == ' ') {
            end--;
        }
        for (int i = end; i >= 0; i--) {
            if (s.charAt(i) != ' ') {
                ans++;
            } else {
                break;
            }
        }
        return ans;
    }
}
// @lc code=end