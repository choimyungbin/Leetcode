import java.util.HashMap;

class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> hashMapS = new HashMap<>();
        HashMap<Character, Integer> hashMapT = new HashMap<>();
        
        for (char c : s.toCharArray()) {
            hashMapS.put(c, hashMapS.getOrDefault(c, 0) + 1);
        }
        
        for (char c : t.toCharArray()) {
            hashMapT.put(c, hashMapT.getOrDefault(c, 0) + 1);
        }
        
        return hashMapS.equals(hashMapT);
    }
}