package javaSolutions;

// Maximum Depth Problem
// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

public class maximumDepthBinaryTree {
  public static int maxDepth(TreeNode root) {
    // if there is no children, our base case
    if (root == null) {
      return 0;
    // if there is a left or right child, keep going down it until you reach a leaf, and then return the bigger of the two depths
    } else {
      return Math.max(maxDepth(root.left) + 1, maxDepth(root.right) + 1);
    }
  }

  public static void main(String[] args) {
    TreeNode root = new TreeNode(1,
            new TreeNode(2, new TreeNode(4), new TreeNode(5)),
            new TreeNode(3, new TreeNode(6), new TreeNode(7))
    );

    // testing that the code works on an arbitrary tree of depth 3.
    System.out.println("The depth of the tree is: " + maxDepth(root));
  }
}


// if you would like to run the above code, please make sure to also have the TreeNode.java file downloaded, as it utilises the class for the purpose of this exercise