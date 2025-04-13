import java.util.Scanner;

public class check_is_prime {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        if (n <= 1) System.out.println("NO");
        boolean isPrime = true;
        for (int i = 2; i * i <= n; i++){
            if (n % i == 0){
                isPrime = false;
                break;
            }
        }
        if (isPrime) System.out.println("YES");
        else System.out.println("NO");
        scanner.close();
    }
}
