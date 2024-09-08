class Solution {
    public String solution(String rsp) {
        String answer = "";
        
        char s = '2';
        char r = '0';
        char p = '5';
        
        for(int i = 0; i < rsp.length(); i++){
            
            if(rsp.charAt(i) == s){
                answer = answer + r;
            }
            else if(rsp.charAt(i) == r){
                answer = answer + p;
            }
            else if(rsp.charAt(i) == p){
                answer = answer + s;
            }
            
        }
        
        return answer;
    }
}