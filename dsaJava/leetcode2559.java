package dsaJava;

public class leetcode2559 {
    public static int maximumCount(int[] nums) {
        int positive = 0, negative = 0;
        for (int num : nums) {
            if (num == 0)
                continue;
            if (num > 0)
                positive++;
            else
                negative++;
        }
        if (positive > negative)
            return positive;
        return negative;
    }

    public static void main(String[] args) {
        System.out.println(maximumCount(new int[] { -3, -2, -1, 0, 1, 2, 3 })); // output 3
        System.out.println(maximumCount(new int[] { -3, -2, -1, 0, 0, 1, 2 })); // output 3
        System.out.println(maximumCount(new int[] { 5, 20, 66, 1314 })); // output 4
    }
}
