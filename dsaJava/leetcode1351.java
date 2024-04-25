package dsaJava;

public class leetcode1351 {
    public static int countNegatives(int[][] grid) {
        int count = 0;
        for (int[] row : grid) {
            for (int i = 0; i < row.length; i++) {
                if (row[i] < 0)
                    count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(
                countNegatives(new int[][] { { 4, 3, 2, -1 }, { 3, 2, 1, -1 }, { 1, 1, -1, -2 }, { -1, -1, -2, -3 } }));// output
                                                                                                                        // 8
        System.out.println(countNegatives(new int[][] { { 3, 2 }, { 1, 0 } })); // output 0
    }
}
