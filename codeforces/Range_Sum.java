// https://codeforces.com/group/MWSDmqGsZm/contest/326907/problem/D
import java.math.BigInteger;
import java.util.Scanner;

public class Range_Sum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        while (t-- > 0) {
            BigInteger a = scanner.nextBigInteger();
            BigInteger b = scanner.nextBigInteger();

            if (a.compareTo(b) > 0) {
                BigInteger temp = a;
                a = b;
                b = temp;
            }

            BigInteger sumB = b.multiply(b.add(BigInteger.ONE)).divide(BigInteger.TWO);
            BigInteger sumA = a.multiply(a.add(BigInteger.ONE)).divide(BigInteger.TWO);
            BigInteger result = sumB.subtract(sumA);

            System.out.println(result.add(a));
        }
        scanner.close();
    }
}

