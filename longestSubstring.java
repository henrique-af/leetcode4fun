import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int a = 0;
        int b = 0;
        int max = 0;

        HashSet<Character> hashSet = new HashSet<>();

        while (b < s.length()) {
            if (!hashSet.contains(s.charAt(b))) {
                hashSet.add(s.charAt(b));
                b++;
                max = Math.max(hashSet.size(), max);
            } else {
                hashSet.remove(s.charAt(a));
                a++;
            }
        }
        return max;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        String inputString = "pwwkew";
        System.out.println(sol.lengthOfLongestSubstring(inputString));
    }
}