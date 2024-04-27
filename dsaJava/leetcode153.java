package dsaJava;

public class leetcode153 {
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
        System.out.println(findMin(new int[] { 3, 4, 5, 1, 2 }));// output 1
        System.out.println(findMin(new int[] { 4, 5, 6, 7, 0, 1, 2 }));// output 0
        System.out.println(findMin(new int[] { 11, 13, 15, 17 }));// output 11
    }
}
