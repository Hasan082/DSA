import java.util.Scanner;

public class Sequence_of_Numbers_and_Sum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int m = scanner.nextInt();
            int n = scanner.nextInt();
            int sum = 0;
            if (m <= 0 || n <= 0) break;
            for (int i = Math.min(m, n); i <= Math.max(m, n); i++) {
                sum += i;
                System.out.print(i + " ");
            }
            System.out.println("sum =" + sum);
        }
        
        scanner.close();
    }
}
