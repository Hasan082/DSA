package dsaJava;

public class leetcode1684 {
    private static boolean isConsistent(String word, String allowed) {
        for (char c : word.toCharArray()) {
            if (!allowed.contains(Character.toString(c))) {
                return false;
            }
        }
        return true;
    }

    public static int countConsistentStrings(String allowed, String[] words) {
        int count = 0;
        for (String word : words) {
            if (isConsistent(word, allowed)) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String[] a = { "n", "eeitfns", "eqqqsfs", "i", "feniqis", "lhoa", "yqyitei", "sqtn", "kug", "z", "neqqis" };
        System.out.println(countConsistentStrings("fstqyienx", a)); // output 8
    }
}
