/*
 * @lc app=leetcode.cn id=283 lang=java
 *
 * [283] 移动零
 */

// @lc code=start
class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length == 1 || nums.length == 0) {
            return ;
        }
        int fast = 0;
        int slow = 0;
        while (slow < nums.length && nums[slow] != 0) {
            slow++;
        }
        fast = slow + 1;
        while (fast < nums.length) {
            if (nums[fast] != 0) {
                nums[slow] = nums[fast];
                nums[fast] = 0;
                slow++;
            }
            fast++;
        }
    }
}
// @lc code=end

