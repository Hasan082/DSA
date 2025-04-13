import java.math.BigInteger;
import java.util.Scanner;

public class Max {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        int max = 0;
        while (t-- > 0) {
            int a = scanner.nextInt();
            if (a > max) {
                max = a;
            }
        }
        System.out.println(max);
    }
}
