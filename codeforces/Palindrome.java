import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        int copy = t, rev = 0;
        while (t > 0) {
            int rem = t % 10;
            t /= 10;
            rev = rev * 10 + rem;
        }

        System.out.println(rev);

        if (rev == copy) System.out.println("YES");
        else System.out.println("NO");
        
        scanner.close();
    }
}
