package dsaJava;

public class leetcode154 {
    public static int findMin(int[] nums) {
        int min = 5000;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < min) {
                min = nums[i];
            }
        }
        return min;
    }

    public static void main(String[] args) {
        System.out.println(findMin(new int[] { 1, 3, 5 })); // output 1
        System.out.println(findMin(new int[] { 2, 2, 2, 0, 1 }));// output 0
    }
}
