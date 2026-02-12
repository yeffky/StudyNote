/*
 * @lc app=leetcode.cn id=160 lang=java
 *
 * [160] 相交链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
public class ListNode {
int val;
ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
// class ListNode {
//     int val;
//     ListNode next;

//     ListNode(int x) {
//         val = x;
//         next = null;
//     }
// }
class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // ListNode curA = headA;
        // ListNode curB = headB;
        // while (curA != curB) {
        //     if (curA != null) {
        //         curA = curA.next;
        //     }
        //     else {
        //         curA = headB;
        //     }
        //     if (curB != null) {
        //         curB = curB.next;
        //     }
        //     else {
        //         curB = headA;
        //     }
        // }
        // return curA;
        ListNode curA = headA;
        ListNode curB = headB;
        while (curA != null) {
            while (curB != null) {
                if (curB == curA) {
                    return curA;
                }
                curB = curB.next;
            }
            curA = curA.next;
            curB = headB;
        }
        return curA;
    }
}
// @lc code=end

