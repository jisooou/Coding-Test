class Solution {
    public int solution(String my_string, String is_suffix) {

        if( is_suffix.length() > my_string.length() ){
            return 0;
        }
        
        for(int i = 0; i < my_string.length(); i++){
            String str = my_string.substring(i, my_string.length());
            if(str.equals(is_suffix)){
                return 1; 
            }
        }
        
        return 0; 
    }
}