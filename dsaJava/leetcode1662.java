package dsaJava;

public class leetcode1662 {
    public static boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringBuilder s1 = new StringBuilder();
        StringBuilder s2 = new StringBuilder();
        for (String a : word1)
            s1.append(a);
        for (String b : word2)
            s2.append(b);
        return s2.toString().equals(s1.toString());
    }

    public static void main(String[] args) {
        System.out.println(arrayStringsAreEqual(new String[] { "ab", "c" }, new String[] { "a", "bc" })); // output true
        System.out.println(arrayStringsAreEqual(new String[] { "a", "cb" }, new String[] { "ab", "c" }));// output false
        System.out.println(arrayStringsAreEqual(new String[] { "abc", "d", "defg" }, new String[] { "abcddefg" }));// output
                                                                                                                   // true
    }
}
