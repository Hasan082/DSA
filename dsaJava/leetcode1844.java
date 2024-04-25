package dsaJava;

public class leetcode1844 {
    public static String replaceDigits(String s) {
        char[] c = s.toCharArray();
        for (int i = 1; i < c.length; i += 2) {
            c[i] = (char) (c[i - 1] + (c[i] - '0'));
        }
        return new String(c);
    }

    public static void main(String[] args) {
        System.out.println(replaceDigits("a1c1e1"));// output "abcdef"
        System.out.println(replaceDigits("a1b2c3d4e"));// output "abbdcfdhe"
        System.out.println(replaceDigits("v0g6s4d"));// output "vvgmswd"
    }
}
