class Solution {
    public boolean isValid(String s) {
        int n= s.length();
        if(n%2==1){return false;}
        
        Map<Character, Character> map = new HashMap<Character, Character>(){{
            put(')','(');
            put(']', '[');
            put('}','{');
        }};
        
        Deque<Character> stack =new LinkedList<Character>();
        for(int i=0; i<n;i++){
            char ch=s.charAt(i);
            if(map.containsKey(ch)){
                if(stack.isEmpty()||stack.peek()!=map.get(ch)){
                    return false;
                }
                stack.pop();
            }else {stack.push(ch);}
        }
        return stack.isEmpty();
    }
}