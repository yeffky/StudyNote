/*
 * @lc app=leetcode.cn id=11 lang=java
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int max_area = 0;
        int cur_area = 0;
        while (left < right) {
            cur_area = (right - left) * Math.min(height[left], height[right]);
            max_area = Math.max(max_area, cur_area);
            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
        }
        return max_area;
    }
}
// @lc code=end

