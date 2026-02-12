/*
 * @Author: yeffky
 * @Date: 2025-09-16 14:36:45
 * @LastEditTime: 2025-09-18 09:27:05
 */
/*
 * @lc app=leetcode.cn id=234 lang=java
 *
 * [234] 回文链表
 */


//  * Definition for singly-linked list.
// class ListNode {
//     int val;
//     ListNode next;
//     ListNode() {}
//     ListNode(int val) { this.val = val; }
//     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
// }

class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode pre = new ListNode();
        ListNode p = new ListNode();
        ListNode pn = new ListNode();
        ListNode newHead = new ListNode(head.val);
        ListNode p2 = newHead;
        p = head;
        pre = null;

        while (p != null) {
            pn = p.next;
            if (pn != null) {
                p2.next = new ListNode(pn.val);
                p2 = p2.next;
            }
            p.next = pre;
            pre = p;
            p = pn;
            
        }
        while (newHead != null && pre != null) {
            if (newHead.val != pre.val) {
                return false;
            }
            newHead = newHead.next;
            pre = pre.next;
        }
        return true;
    }
}
// @lc code=end

