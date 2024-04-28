package dsaJava;

import java.util.Arrays;

public class leetcode2433 {
    public static int[] findArray(int[] pref) {
        int n = pref.length;
        int[] arr = new int[n];
        arr[0] = pref[0];
        for (int i = 1; i < n; i++) {
            arr[i] = pref[i] ^ pref[i - 1];
        }
        return arr;
    }

    public static void main(String[] args) {
        int[] pref = { 5, 2, 0, 3, 1 };
        System.out.println(Arrays.toString(findArray(pref)));
    }
}
