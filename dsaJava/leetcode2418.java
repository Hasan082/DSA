package dsaJava;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class leetcode2418 {
    public static String[] sortPeople(String[] names, int[] heights) {
        Map<Integer, String> myMap = new HashMap<>();
        for (int i = 0; i < heights.length; i++) {
            myMap.put(heights[i], names[i]);
        }
        String[] result = new String[heights.length];
        Arrays.sort(heights);
        for (int i = 0; i < heights.length; i++) {
            result[i] = myMap.get(heights[heights.length - 1 - i]);
        }
        return result;
    }

    public static void main(String[] args) {
        String[] res1 = sortPeople(new String[] { "Mary", "John", "Emma" }, new int[] { 180, 165, 170 });
        System.out.println(Arrays.toString(res1));// output [Mary, Emma, John]
        String[] res2 = sortPeople(new String[] { "Alice", "Bob", "Bob" }, new int[] { 155, 185, 150 });
        System.out.println(Arrays.toString(res2));// output [Bob, Alice, Bob]
    }
}
