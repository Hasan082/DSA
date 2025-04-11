import java.util.Scanner;

public class Sum_of_Consecutive_Odd_Numbers {
public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int t = scanner.nextInt();
    while (t-- > 0) {
        int X = scanner.nextInt();
        int Y = scanner.nextInt();
        int sum = 0;
        if (X > Y) {
            int temp = Y;
            Y = X;
            X = temp;
        }
        for (int i = X + 1; i < Y; i++){
            if (i % 2 == 1) sum += i;
        }
        System.out.println(sum);
    }
    scanner.close();
}
}