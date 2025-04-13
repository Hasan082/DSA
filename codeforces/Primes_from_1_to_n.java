import java.util.Scanner;

public class Primes_from_1_to_n {

    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 1; i <= t; i++) {
            if (isPrime(i)){
                System.out.print(i + " ");
            }
        }

        scanner.close();
    }    
}
