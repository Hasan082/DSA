import java.util.Scanner;

public class SomeSums {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            int temp = i;
            int rem = 0;
            while (temp > 0) {
                rem = i % 10;
                temp /= 10;
            }
            int temSUm = rem + temp;
            if (a <= temSUm && b >= temSUm) {
                System.out.println(i + " " + temSUm);
                sum += i;
            }
        }
        System.out.println(sum);

        scanner.close();
    }
}
