package dsaJava;

public class leetcode33 {
    public static int search(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] nums1 = { 4, 5, 6, 7, 0, 1, 2 };
        System.out.println(search(nums1, 0)); // output 4
        int[] nums2 = { 4, 5, 6, 7, 0, 1, 2 };
        System.out.println(search(nums2, 3)); // output -1
        int[] nums3 = { 1 };
        System.out.println(search(nums3, 3)); // output -1
    }
}
