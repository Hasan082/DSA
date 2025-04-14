import java.util.Arrays;
import java.util.Scanner;

public class drawing_x {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int mid = n / 2;
        for (int i = 0; i < n; i++) {
            char[] line = new char[n];
            Arrays.fill(line, '*');
            if (i == mid) {
                line[i] = 'X';
            } else {
                line[i] = '\\';
                line[n - i - 1] = '/';
            }
            System.out.println(String.valueOf(line));
        }

        scanner.close();
    }
}
