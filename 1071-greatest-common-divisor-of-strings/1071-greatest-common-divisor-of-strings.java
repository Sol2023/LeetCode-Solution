class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int l1 = str1.length();
        int l2 = str2.length();

        for(int i= Math.min(l1, l2); i>0; i--) {
            if( valid(i, str1, str2, l1, l2) ){
                return str1.substring(0,i);
            }

            
        }

        return "";
    }

    public Boolean valid(int i, String str1, String str2, int l1, int l2) {
        if(l1 % i > 0 || l2 % i > 0) {
            return false;
        }


        String base = str1.substring(0,i);

        return str1.replace(base, "").isEmpty() && str2.replace(base, "").isEmpty();
    }
}