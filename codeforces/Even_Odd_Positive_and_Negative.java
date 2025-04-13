import java.util.Scanner;

public class Even_Odd_Positive_and_Negative {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        int even = 0, pos = 0, neg = 0;
        for (int i = 0; i < t; i++) {
            int a = scanner.nextInt();
            if (a % 2 == 0) even++;
            if (a > 0) pos++;
            if (a < 0) neg++;
        }
        System.out.println("Even: " + even);
        System.out.println("Odd: " + (t - even));
        System.out.println("Positive: " + pos);
        System.out.println("Negative: " + neg);

        scanner.close();
    }
}
