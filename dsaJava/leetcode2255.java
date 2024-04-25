package dsaJava;

public class leetcode2255 {
    public static int countPrefixes(String[] words, String s) {
        int count = 0;
        for (String word : words) {
            if (s.startsWith(word))
                count++;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(countPrefixes(new String[] { "a", "b", "c", "ab", "bc", "abc" }, "abc"));
        System.out.println(countPrefixes(new String[] { "a", "a" }, "aa"));
    }
}
