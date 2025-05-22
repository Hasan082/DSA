import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class Construct {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        System.out.println("ANSWER IS BELOW");
        while (t-- > 0) {
            long n = scanner.nextLong();
            long s = scanner.nextLong();
            long[] a = new long[(int) n];
            for (int i = 1; i <= a.length; i++) {
                a[i - 1] = i;
            }

            long totalsum = (n * (n + 1)) / 2;
            if (totalsum < s || s <= 2) {
                System.out.println(-1);
            } else if (n >= s) {
                System.out.println((s - 1) + " " + 1);
            } else {
                int sum = 0;
                int index = 0;
                for(int i = 0; i < a.length; i ++) {
                    sum += i;
                    if (s == sum) {
                        index = i;
                    }
                }
                System.out.println("index: " + index);
            }

        }
        scanner.close();
    }
}
