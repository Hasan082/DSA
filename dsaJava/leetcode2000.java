package dsaJava;

public class leetcode2000 {
    public static String reversePrefix(String word, char ch) {
        char[] c = word.toCharArray();
        int findIndex = word.indexOf(ch);
        if(findIndex != -1){
            StringBuilder half = new StringBuilder(word.substring(0, findIndex + 1));
            return half.reverse().toString() + word.substring(findIndex+1);
        }
        return word;
    }
    public static void main(String[] args) {
        System.out.println(reversePrefix("abcdefd", 'd'));
        System.out.println(reversePrefix("xyxzxe", 'z'));
        System.out.println(reversePrefix("abcd", 'z'));

    }
}
