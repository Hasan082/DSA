import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int N = scanner.nextInt();
            long fact = 1;
            for (int j = 2; j <= N; j++) {
                fact *= j;
            }
            System.out.println(fact);
        }

        scanner.close();
    }
}
