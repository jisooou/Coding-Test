import java.util.*;
class Solution {
    public long solution(long n) {
        
        /*
        1. n을 하나씩 잘라서 배열에 넣는다 .
        2. Arrays.sort를 이용해서 내림차순으로 정렬한다. 
        3. 배열 > 정수형으로 바꾼다. (long)
        배열 > 문자열 > 정수
        */
        
        long answer = 0;
        
        String[] array = Long.toString(n).split("");
        Arrays.sort(array, Collections.reverseOrder());
        
        String result = "";
        for(String s : array){
            result = result + s;
        }
        answer = Long.parseLong(result);
        
        return answer;
        
    }
}