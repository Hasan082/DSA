package dsaJava;

public class leetcode2185 {
    public static int prefixCount(String[] words, String pref) {
        int count = 0;
        for (String s : words) {
            if (s.startsWith(pref))
                count++;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(prefixCount(new String[] { "pay", "attention", "practice", "attend" }, "at")); // output 2
        System.out.println(prefixCount(new String[] { "leetcode", "win", "loops", "success" }, "code")); // output 0
    }
}
