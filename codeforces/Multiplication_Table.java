import java.util.Scanner;

public class Multiplication_Table {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 1 ; i <= 12; i++) {
            System.out.println(t +" * " + i +" = " + (t * i));
        }

        scanner.close();
    }
}
