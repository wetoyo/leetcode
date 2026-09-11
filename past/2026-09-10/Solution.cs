// LeetCode #2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
//
// Difficulty: Medium
// Topics: Tree, Depth-First Search, Binary Tree
//
// Approach:
//
// Time:  O(n?)
// Space: O(n?)
// not sure about the complexity, but each node is explored only once, so I believe that it is o(n)
public class Solution {
    public int count = 0;

    public int AverageOfSubtree(TreeNode root) {
        Recurse(root);
        return count;
    }

    public (int, int) Recurse(TreeNode root) {
        if (root == null) return (0, 0);

        (int, int) left = Recurse(root.left);
        (int, int) right = Recurse(root.right);

        int sum = left.Item1 + right.Item1 + root.val;
        int nodes = left.Item2 + right.Item2 + 1;

        if (sum / nodes == root.val)
            count++;

        return (sum, nodes);
    }
}
