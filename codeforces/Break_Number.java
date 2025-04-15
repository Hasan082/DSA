import java.util.Scanner;

public class Break_Number {
    public static int divisble(long a, int count) {
        if (a % 2 != 0) return count;
        return divisble(a / 2, count + 1);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int count = 0;
        long max = 0;
        while (n-- > 0) {
            long a = scanner.nextLong();
            long res = divisble(a, count);
            max = Math.max(res, max);
        }
        System.out.println(max);
        scanner.close();
    }
}
