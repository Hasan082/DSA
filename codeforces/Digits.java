import java.util.Scanner;

public class Digits {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        while (t-- > 0) {
            int a = scanner.nextInt();
            if(a == 0){
                System.out.print("0");
            }
            while (a>0) {
                int rem = a % 10;
                a /= 10; 
                System.out.print(rem + " ");
            }
            System.out.println();
        }
        scanner.close();
    }
}
