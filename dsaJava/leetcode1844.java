package dsaJava;

public class leetcode1844 {
    public static String replaceDigits(String s) {
        char[] c = s.toCharArray();
        for(int i = 1; i< c.length; i+=2){  
            c[i] = (char) (c[i -1] + (c[i] - '0'));
        }
        return new String(c);
    }
    public static void main(String[] args) {
        System.out.println(replaceDigits("a1c1e1"));
        System.out.println(replaceDigits("a1b2c3d4e"));
        System.out.println(replaceDigits("v0g6s4d"));       
    }
}
