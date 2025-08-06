package javaSolutions;

// below is the defined TreeNode class

public class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  // if we have an empty node without anything associated with it
  TreeNode() {}

  // if we have a tree node that is a leaf
  TreeNode(int val) { 
    this.val = val; 
  }

  // if we have a tree node that has left or right children
  TreeNode(int val, TreeNode left, TreeNode right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}
