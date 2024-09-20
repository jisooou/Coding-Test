class Solution {
    public boolean solution(String s) {
        /*
        1. s의 길이만큼 문자열을 돌면서 
        2. 알파벳인지 확인 > Character.isAlphabetic()
        3. 알파벳이 있을 때마다 count 한 후에
        4. 마지막 count 개수에 따라 true와 false를 리턴 
            *숫자( Character.isDigit() )인지 알파벳인지 판단
        */
        boolean answer = true;
        boolean error = false;
        int count = 0; 
        
        if(s.length() != 4 && s.length() != 6){
            return error; 
        }
        
        for(int i = 0; i < s.length(); i++){
            if( Character.isAlphabetic(s.charAt(i)) ){
                count++; 
            }
        }
        if(count > 0){
            return error;
        }
        return answer;
    }
}