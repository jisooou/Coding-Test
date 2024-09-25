import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
         /*
            각 단어의 n번째 문자를 기준으로 정렬 
                > n을 문자열 앞에 추가 후 sort
        */
        String[] answer = new String[strings.length];
        List<String> list = new ArrayList<>();
        
        for(int i = 0; i < strings.length; i++){
            //strings[i].charAt(n) > u, e, a 
            list.add(strings[i].charAt(n) + strings[i]); 
        }
        
        
        Collections.sort(list); //acar, ebed, usun 
        
        for(int i = 0; i < list.size(); i++){
            answer[i] = list.get(i).substring(1, list.get(i).length());
        }
        
        return answer;
    }
}