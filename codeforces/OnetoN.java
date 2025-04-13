import java.util.Scanner;

public class OnetoN {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 1; i <= t; i++) {
            System.out.println(i);
        }
        scanner.close();
    }
}
