package dsaJava;

public class leetcode2317 {
    public static int maximumXOR(int[] nums) {
        if (nums.length < 2)
            return nums[0];
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            res |= nums[i];
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(maximumXOR(new int[] { 3, 2, 4, 6 }));
    }
}
