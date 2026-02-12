/*
 * @Author: yeffky 18850466266@163.com
 * @Date: 2025-05-08 10:39:10
 * @LastEditors: yeffky 18850466266@163.com
 * @LastEditTime: 2025-05-13 10:58:25
 * @FilePath: \Study\LeetCode\Main.java
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */


class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }
        if (list1!= null) {
            current.next = list1;
        } else {
            current.next = list2;
        }
        return dummy.next;
    }
}

public class Solution21 {
    public static void main(String[] args) {
        ListNode list1 = new ListNode(1);
        
        
        ListNode list2 = new ListNode(2);

        Solution solution = new Solution();
        ListNode mergedList = solution.mergeTwoLists(list1, list2);

        // 打印合并后的链表
        while (mergedList != null) {
            System.out.print(mergedList.val + " ");
            mergedList = mergedList.next;
        }
    }
}