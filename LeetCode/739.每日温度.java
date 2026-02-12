/*
 * @Author: yeffky
 * @Date: 2025-09-18 09:36:12
 * @LastEditTime: 2025-09-18 10:30:13
 */
/*
 * @lc app=leetcode.cn id=739 lang=java
 *
 * [739] 每日温度
 */

// @lc code=start

import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        // int[] result = new int[temperatures.length];
        // result[temperatures.length - 1] = 0;
        // for (int i = 0; i < temperatures.length - 1; i++) {
        //     for (int j = i + 1; j < temperatures.length; j++) {
        //         if (temperatures[j] > temperatures[i]) {
        //             result[i] = j - i;
        //             break;
        //         }
        //         if (j == temperatures.length - 1) {
        //             result[i] = 0;
        //             break;
        //         }
        //     }
            
        // }
        // return result;
        int length = temperatures.length;
        int[] ans = new int[length];
        int[] next = new int[101];
        Arrays.fill(next, Integer.MAX_VALUE);
        for (int i = length - 1; i >= 0; --i) {
            int warmerIndex = Integer.MAX_VALUE;
            for (int t = temperatures[i] + 1; t <= 100; t++) {
                if (next[t] < warmerIndex) {
                    warmerIndex = next[t];
                }
            }
            if (warmerIndex < Integer.MAX_VALUE) {
                ans[i] = warmerIndex - i;
            }
            next[temperatures[i]] = i;
        }
        return ans;
    }
}
// @lc code=end
