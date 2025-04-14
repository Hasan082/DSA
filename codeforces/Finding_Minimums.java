import java.util.*;

public class Finding_Minimums {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(), k = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }

        int i = 0;
        while (i < n) {
            int min = Integer.MAX_VALUE;
            int j = i;
            while(j < i + k && j < n) {
                min = Math.min(min, a[j]);
                j++;
            }
            System.out.print(min + " ");
            i += k;
        }
        scanner.close();
    }
}
