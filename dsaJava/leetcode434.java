package dsaJava;

public class leetcode434 {
    public static int countSegments(String s) {
        if (s.length() < 1)
            return 0;
        int segment = 0;
        for (int i = 0; i < s.length(); i++) {
            if ((i == 0 || s.charAt(i - 1) == ' ') && s.charAt(i) != ' ') {
                segment++;
            }
        }
        return segment;
    }

    public static void main(String[] args) {
        System.out.println(countSegments("Hello, my name is John"));// output 5
    }
}
