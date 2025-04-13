import java.util.Scanner;

public class Shape1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        String sym = "*";
        for(int i = t; i >0; i--) {
            System.out.println(sym.repeat(i));
        }
        scanner.close();
    }
}
