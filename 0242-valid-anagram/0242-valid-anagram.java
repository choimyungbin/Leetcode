import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> hashMapS = new HashMap();
        Map<Character, Integer> hashMapT = new HashMap();
        
        for (char c:s.toCharArray()){
            hashMapS.put(c, hashMapS.getOrDefault(c, 0)+1);
        }
        for (char c:t.toCharArray()){
            hashMapT.put(c, hashMapT.getOrDefault(c, 0)+1);
        }
        return hashMapS.equals(hashMapT);
    }
}