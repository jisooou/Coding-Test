import java.util.*;
class Solution {
    public long solution(long n) {
        /*
        <첫 번째 방법>
        함수를 사용하지 않고, 10으로 나누었을 때 나머지를 사용해서 풀이 
        1.n을 10으로 나눈 나머지의 각 숫자를 리스트에 저장 
        2.리스트 내에서 내림차순으로 정렬 
        3.정렬한 값을 정수로 다시 변경
        */
        ArrayList<Long> array = new ArrayList<>();
        
        while(n > 0){
            array.add(n % 10);
            n = n / 10; 
        }
        
        Collections.sort(array, Collections.reverseOrder());
        
        long answer = 0; 
        for(long num : array){
            answer = answer * 10 + num;
        }
        
        return answer;
        
        /*
        <두 번째 방법>
        1. n을 하나씩 잘라서 배열에 넣는다 .
        2. Arrays.sort를 이용해서 내림차순으로 정렬한다. 
        3. 배열 > 정수형으로 바꾼다. (long)
        배열 > 문자열 > 정수
        */
        /*
        long answer = 0;
        
        String[] array = Long.toString(n).split("");
        Arrays.sort(array, Collections.reverseOrder());
        
        String result = "";
        for(String s : array){
            result = result + s;
        }
        answer = Long.parseLong(result);
        
        return answer;
        */
    }
}