package dsaJava;

import java.util.Arrays;

public class leetcode1051 {
    public static void main(String[] args) {

        System.out.println(heightChecker(new int[] { 1, 1, 4, 2, 1, 3 }));
        System.out.println(heightChecker(new int[] { 5, 1, 2, 3, 4 }));
        System.out.println(heightChecker(new int[] { 1, 2, 3, 4, 5 }));
    }

    public static int heightChecker(int[] heights) {
        int count = 0;
        int[] secHeight = new int[heights.length];
        for (int i = 0; i < heights.length; i++) {
            secHeight[i] = heights[i];
        }
        Arrays.sort(heights);
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != secHeight[i])
                count++;
        }
        return count;

    }
}
