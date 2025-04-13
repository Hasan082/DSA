import java.util.Scanner;

public class Shape2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int rows = scanner.nextInt();
        String sym = "*";
        int maxStar = rows * 2 - 1;
        for (int i = 0; i < rows; i++) {
            int stars = i * 2 + 1;
            int line = (maxStar - stars) / 2;
            System.out.println(" ".repeat(line) + sym.repeat(stars));
        }
        scanner.close();
    }
}
