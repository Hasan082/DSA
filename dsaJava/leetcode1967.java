package dsaJava;

public class leetcode1967 {
    public static int numOfStrings(String[] patterns, String word) {
        int count = 0;
        for(String p: patterns){
            if(word.contains(p))count++;
        }
        return count;
    }
    public static void main(String[] args) {
        String[] patterns = {"a","abc","bc","d"};
        String word = "abc";
        System.out.println(numOfStrings(patterns, word));

        String[] patterns1 = {"a","b","c"};
        String word1 = "aaaaabbbbb";
        System.out.println(numOfStrings(patterns1, word1));
    }
}
