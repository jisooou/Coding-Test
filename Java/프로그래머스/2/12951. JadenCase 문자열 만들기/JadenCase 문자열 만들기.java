class Solution {
    public String solution(String s) {
        /*
        1. 문자열을 소문자로 바꾼다.
        2. 문자열 s를 돈다.
        3. s를 도는 동안 공백 문자를 찾는다. 
        4. (알파벳일 경우) 공백 문자 다음 인덱스를 대문자로 바꿔준다. 
        5. (알파벳이 아닐 경우) 바꾸지 않는다.
        6. answer에 저장해 준 후 리턴한다.
        */
        
        String answer = "";
        s = s.toLowerCase();
        
        for(int i = 0; i < s.length(); i++){
            
            char word = s.charAt(i);
            if( i == 0 || s.charAt(i-1) == ' ' ){
                if( Character.isLetter(word) ){
                    answer += Character.toUpperCase(word);
                }
                else{
                    answer += word; 
                }
            }
            else{
                answer += word; 
            }

        }
        
        return answer;
    }
}