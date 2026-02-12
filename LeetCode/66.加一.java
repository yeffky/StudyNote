/*
 * @lc app=leetcode.cn id=66 lang=java
 *
 * [66] 加一
 */

// @lc code=start
class Solution {
    public int[] plusOne(int[] digits) {
        int flag = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] == 9 && flag == 1) {
                digits[i] = 0;
                flag = 1;
            } else {
                digits[i]++;
                flag = 0;
                return digits;
            }
        }
        if (flag == 1) {
            int result[] = new int[digits.length + 1];
            result[0] = 1;
            for (int i = 0; i < digits.length; i++) {
                result[i + 1] = digits[i];
            }
            return result;
        }
        return digits;
    }
}
// @lc code=end
