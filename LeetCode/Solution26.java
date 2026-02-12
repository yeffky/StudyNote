/*
 * @Author: yeffky 18850466266@163.com
 * @Date: 2025-05-13 10:58:33
 * @LastEditors: yeffky 18850466266@163.com
 * @LastEditTime: 2025-05-13 11:23:10
 * @FilePath: \Study\LeetCode\Solution26.java
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
class Solution {
    public int removeDuplicates(int[] nums) {
        // int[] flags = new int[20020];
        // int j = 0;
        // for(int i = 0;i<nums.length;i++){
        //     if (flags[nums[i] + 10010] == 0){
        //         flags[nums[i] + 10010] = 1;
        //         nums[j] = nums[i];
        //         j++;
        //     }
        // }
        // return j;

        int slow = 1;
        for (int fast = 1; fast < nums.length; fast++) {
            if (nums[fast] != nums[slow - 1]) {
                nums[slow] = nums[fast];
                slow++;
            }
        }
        return slow;
    }
}

public class Solution26 {
    public static void main(String[] args) {
        int[] nums = {0,0,1,1,1,2,2,3,3,4};
        int[] expectedNums = {0,1,2,3,4};
        
        Solution solution = new Solution();
        int k = solution.removeDuplicates(nums);
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i]+" ");
        }
        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
    }
}