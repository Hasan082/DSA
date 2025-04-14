import java.util.Scanner;

public class Lucky_Numbers {
    public static boolean isLucky(int n) {
        while (n > 0) {
            int rem = n % 10;
            if (rem != 4 && rem != 7) {
                return false;
            }
            n /= 10;
        }
        return true;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int start = scanner.nextInt();
        int end = scanner.nextInt();
        int count = 0;

        for(int i = start; i <= end; i++){
            if(isLucky(i)) {
                System.out.print(i + " ");
                count++;
            }
        }

        if (count==0) System.out.println(-1);
        scanner.close();
    }
}
