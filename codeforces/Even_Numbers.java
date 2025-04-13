import java.util.Scanner;

public class Even_Numbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        if (t == 1) System.out.println(-1);
        for (int i = 1; i <= t; i ++) {
            if (i % 2 == 0){
                System.out.println(i);
            };
        }
        scanner.close();
    }
}
