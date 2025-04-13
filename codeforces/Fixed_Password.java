import java.util.Scanner;

public class Fixed_Password {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int pass = scanner.nextInt();
            if (pass != 1999) System.out.println("Wrong");
            else {
                System.out.println("Correct");
                break;
            }
        }
        scanner.close();
        
    }
}
