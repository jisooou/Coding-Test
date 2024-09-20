import java.util.*;
class Solution {
    public String solution(String s) {
        /*
        1. 알파벳 역순으로 리턴
        2. 대문자는 맨끝에 리턴 (대문자도 역순으로 리턴)
        */
        String answer = "";
        
        //소문자일 때
        for(char c = 'z'; c >= 'a'; c--){
            for(int i = 0; i < s.length(); i++){
                //s의 인덱스와 해당 알파벳이 일치할 때
                if(s.charAt(i) == c){
                    answer = answer + s.charAt(i);
                }
            }
        }

        
        //대문자일 때
        for(char x = 'Z'; x >= 'A'; x--){
            for(int y = 0; y < s.length(); y++){
                if(s.charAt(y) == x){
                    answer = answer + s.charAt(y);
                }
            }
        }

        
        return answer;
    }
}