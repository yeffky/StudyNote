/*
 * @Author: yeffky
 * @Date: 2025-09-16 09:54:06
 * @LastEditTime: 2025-09-16 10:57:14
 */
/*
 * @lc app=leetcode.cn id=236 lang=java
 *
 * [236] 二叉树的最近公共祖先
 */

// @lc code=start


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode lres = null;
        TreeNode rres = null;
        if (root == null) {
            return null;
        }
        lres = lowestCommonAncestor(root.left, p, q);
        rres = lowestCommonAncestor(root.right, p, q);
        if (root.val == p.val || root.val == q.val) {
            return root;
        }
        if (lres != null && rres != null) {
            return root;
        }
        else if (lres !=null && rres == null) {
            return lres;
        }
        else if (rres !=null && lres == null){
            return rres;
        }
        return null;
    }
}
// @lc code=end
