
import java.util.Scanner;

public class Hady_Rides_the_Train {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long row = n / 4;
        System.out.print(row + " ");
        if (row % 2 == 0) {
            System.out.print(n % 4);
        } else {
            System.out.print(3 - (n % 4));
        }
        scanner.close();
    }
}
