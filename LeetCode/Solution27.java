/*
 * @Author: yeffky 18850466266@163.com
 * @Date: 2025-05-13 15:11:15
 * @LastEditors: yeffky 18850466266@163.com
 * @LastEditTime: 2025-05-13 15:16:13
 * @FilePath: \Study\LeetCode\Solution27.java
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */

import java.util.Arrays;

class Solution {
    public int removeElement(int[] nums, int val) {
        int slow = 0;
        for (int fast = 0; fast < nums.length; fast++) {
            if (nums[fast]!= val) {
                nums[slow] = nums[fast];
                slow++;
            }
        }
        return slow;
    }
}


public class Solution27 {
    public static void main(String[] args) {
        int[] nums = {0,1,2,2,3,0,4,2};
        int val = 2;
        int[] expectedNums = {0,1,4,0,3};
        Solution solution = new Solution();
        int k = solution.removeElement(nums, val);
        for (int i = 0; i < k; i++) {
            System.out.println(nums[i]);
        }   
        assert k == expectedNums.length;
        Arrays.sort(nums, 0, k);
        for (int i = 0; i < expectedNums.length; i++) {
            assert nums[i] == expectedNums[i];
        }
    }
    
}
