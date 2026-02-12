/*
 * @Author: yeffky
 * @Date: 2025-06-11 14:54:13
 * @LastEditTime: 2025-06-26 16:09:25
 */
/*
 * @lc app=leetcode.cn id=128 lang=java
 *
 * [128] 最长连续序列
 */

// @lc code=start

import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int longestConsecutive(int[] nums) {
        // if (nums.length == 0) {
        // return 0;
        // }
        // int[] ans = new int[10000000];
        // Arrays.fill(ans, 0);
        // int max = -Integer.MAX_VALUE;
        // int min = Integer.MAX_VALUE;
        // for (int i = 0; i < nums.length; i++) {
        // ans[nums[i] + 1000] = 1;
        // if (nums[i] + 1000 > max) {
        // max = nums[i] + 1000;
        // }
        // if (nums[i] + 1000 < min) {
        // min = nums[i] + 1000;
        // }
        // }
        // int maxLen = 1;
        // int temLen = 1;
        // for (int i = min; i < max; i++) {
        // if (ans[i] != 0 && ans[i + 1] != 0) {
        // temLen++;
        // if (temLen > maxLen) {
        // maxLen = temLen;
        // }
        // } else {
        // temLen = 1;
        // }
        // }
        // return maxLen;
        if (nums.length == 0) {
            return 0;
        }
        Set<Integer> set = new HashSet<>();
        int max_len = 1;
        int tmp_len = 1;
        for (int num : nums) {
            set.add(num);
        }
        for (int num : set) {
            if (set.contains(num - 1)) {
                continue;
            } else {
                while (set.contains(num + 1)) {
                    num++;
                    tmp_len++;
                }
                if (tmp_len > max_len) {
                    max_len = tmp_len;
                }
                tmp_len = 1;
            }
        }
        return max_len;
    }
}
// @lc code=end
