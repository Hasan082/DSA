package dsaJava;

public class leetcode81 {
    public static boolean search(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(search(new int[] { 2, 5, 6, 0, 0, 1, 2 }, 0));// output true
        System.out.println(search(new int[] { 2, 5, 6, 0, 0, 1, 2 }, 3));// output false
    }
}
