import java.util.Arrays;
import java.util.HashSet;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        HashSet<Character> hashSet = new HashSet<>(Arrays.asList('(', '[', '{'));
        Stack<Character> stack = new Stack<>();
        
        for (Character c : s.toCharArray()) {
            if (hashSet.contains(c)) {
                stack.push(c);
            } else {
                
                if (stack.isEmpty()) {
                    return false;
                }
                
                if (c.equals(')') && stack.peek().equals('(')) {
                    stack.pop();
                } else if (c.equals('}') && stack.peek().equals('{')) {
                    stack.pop();
                } else if (c.equals(']') && stack.peek().equals('[')) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
