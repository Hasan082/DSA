import java.util.Scanner;

public class Numbers_Histogram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String sym = scanner.next();
        int t = scanner.nextInt();
        while (t-- > 0) {
            int input = scanner.nextInt();
            System.out.println(sym.repeat(input));
        }
        scanner.close();
    }
}
