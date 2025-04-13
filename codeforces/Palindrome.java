import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        int copy = t;
        String s = "";
        while (t > 0) {
            int rem = t % 10;
            t /= 10;
            s+=rem;
        }

        int rev = Integer.parseInt(s);
        System.out.println(rev);

        if (rev == copy) System.out.println("YES");
        else System.out.println("NO");
        scanner.close();
    }
}
