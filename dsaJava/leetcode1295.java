package dsaJava;

public class leetcode1295 {
    public static int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            String s = String.valueOf(num);
            if (s.length() % 2 == 0)
                count++;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(findNumbers(new int[] { 12, 345, 2, 6, 7896 }));// output 2
        System.out.println(findNumbers(new int[] { 555, 901, 482, 1771 }));// output 1
    }
}
