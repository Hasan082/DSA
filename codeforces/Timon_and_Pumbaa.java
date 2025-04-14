import java.util.Scanner;

public class Timon_and_Pumbaa {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt(), b = scanner.nextInt();
        if (a - b >= 0) {
            System.out.println(a - b);
        }else {
            System.out.println(0);
        }
        scanner.close();
    }
}
