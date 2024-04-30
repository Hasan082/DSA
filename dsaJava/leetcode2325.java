package dsaJava;

import java.util.HashSet;
import java.util.Set;

public class leetcode2325 {
    public static String decodeMessage(String key, String message) {

        Set<Character> set = new HashSet<>();
        char[] rearr = new char[26];
        int s = 0;
        for(char c : key.toCharArray()){
            if(c != ' ' && !set.contains(c)){
                rearr[s] = c;
                set.add(c);
                s++;
            }
        }
        
        String v = new String(rearr);
        StringBuilder res = new StringBuilder();

        for(int j = 0; j < message.length(); j++) {
            if(message.charAt(j) != ' ') {         
                int findInd = (int) 'a' + v.indexOf(message.charAt(j));
                res.append((char) findInd);
            } else res.append(" ");
        }
        return res.toString();

    }
public static void main(String[] args) {
    String key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv";
    System.out.println(decodeMessage(key, message));
}
}
