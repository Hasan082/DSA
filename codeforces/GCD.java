import java.util.Scanner;

public class GCD {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt(), 
            b = scanner.nextInt();
        int gcd = 0;
        for (int i = 1; i <= Math.max(a, b); i++) {
            if (a % i == 0 && b % i == 0) {
                if (i > gcd) {
                    gcd = i;
                }
            }
        }
        System.out.println(gcd);
        scanner.close();
    }
}
