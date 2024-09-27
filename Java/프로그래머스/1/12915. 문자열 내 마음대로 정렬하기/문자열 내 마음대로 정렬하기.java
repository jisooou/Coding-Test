//아스키 코드, Character.compareTo() 메서드 
import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        
        for (int i = 0; i < strings.length - 1; i++) {
            for (int j = i + 1; j < strings.length; j++) {
                
                //n번째 문자를 비교
                if (strings[i].charAt(n) > strings[j].charAt(n)) {
                    //정렬
                    String temp = strings[i];
                    strings[i] = strings[j];
                    strings[j] = temp;
                } 
                else if (strings[i].charAt(n) == strings[j].charAt(n)) {
                    //예) abce가 abcd보다 앞에 오는 경우 > 다시 정렬 
                    if(strings[i].compareTo(strings[j]) > 0){
                        String temp = strings[i];
                        strings[i] = strings[j];
                        strings[j] = temp;
                    }
                }
            }
        }

        return strings; 
    }
}


//          /*
//             각 단어의 n번째 문자를 기준으로 정렬 
//                 > n을 문자열 앞에 추가 후 sort
//         */
//         String[] answer = new String[strings.length];
//         List<String> list = new ArrayList<>();
        
//         for(int i = 0; i < strings.length; i++){
//             //strings[i].charAt(n) > u, e, a 
//             list.add(strings[i].charAt(n) + strings[i]); 
//         }
        
        
//         Collections.sort(list); //acar, ebed, usun 
        
//         for(int i = 0; i < list.size(); i++){
//             answer[i] = list.get(i).substring(1, list.get(i).length());
//         }
        
//         return answer;