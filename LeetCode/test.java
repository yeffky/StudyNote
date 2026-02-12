/*
 * @Author: yeffky
 * @Date: 2025-06-10 14:04:05
 * @LastEditTime: 2025-09-17 10:00:13
 */

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

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
        // while (newHead != null) {
        //     System.out.println(newHead.val);
        //     newHead = newHead.next;
        // }
        while (newHead != null && pre != null) {
            System.out.println("head:" + newHead.val + "pre" + pre.val);
            if (newHead.val != pre.val) {
                return false;
            }
            newHead = newHead.next;
            pre = pre.next;
        }
        return true;
    }

    public void insertNode(ListNode head, int val) {
        ListNode newNode = new ListNode(val);
        ListNode p = new ListNode();
        ListNode pre = new ListNode();
        p = head.next;
        pre = head;
        while (p != null) {
            pre = p;
            p = p.next;
        }
        pre.next = newNode;
    }
}

public class test {
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        Solution solution = new Solution();
        solution.insertNode(head, 2);
        solution.insertNode(head, 2);
        solution.insertNode(head, 1);
        System.out.println(solution.isPalindrome(head));
    }
}
