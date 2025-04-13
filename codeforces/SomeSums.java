import java.util.Scanner;

public class SomeSums {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        for (int i = 1; i <= n; i++) {
            int temp = i;
            while (temp > 9) {
                int rem = i % 10;
                temp /= 10;
                int sum = rem + temp;
                System.out.println("sum: " + sum);
            }
            if (a <= i & b >= i) {
                System.err.println(i);
            }
        }

        scanner.close();
    }
}
