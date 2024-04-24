package dsaJava;
public class leetcode1859 {

    public static String sortSentence(String s) {
        String[] c = s.split(" ");
        String[] b = new String[c.length];
        for(int i = 0; i < c.length; i++){
            int index = c[i].charAt(c[i].length() - 1) - '0';
            String word = c[i].substring(0, c[i].length() - 1);
            b[index - 1] = word; 
        }
        return String.join(" ", b);
    }

public static void main(String[] args) {
    System.out.println(sortSentence("is2 sentence4 This1 a3"));
    System.out.println(sortSentence("Myself2 Me1 I4 and3"));
}
}
