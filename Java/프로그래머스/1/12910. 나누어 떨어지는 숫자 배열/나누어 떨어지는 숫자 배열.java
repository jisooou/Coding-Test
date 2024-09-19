//ArrayList - size()
import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        /*
        1. ArrayList 사용
        2. arr를 도는 동안, divisior로 나누어 떨어지는 값 찾기 
        3. 나누어 떨어지는 값 X > -1 리턴 
        4. 나누어 떨어지는 값 O > answer 오름차순으로 정렬 후 리턴 
        */
        int[] answer = {};
        ArrayList<Integer> array = new ArrayList<Integer>();
        
        for(int i = 0; i < arr.length; i++){
            if(arr[i] % divisor == 0){
                array.add(arr[i]);
            }
        }
        
        //나누어 떨어지는 값 X
        if(array.size() == 0){
            answer = new int[1];
            answer[0] = -1; 
        }
        //나누어 떨어지는 값 O
        else{
            answer = new int[array.size()];
            Collections.sort(array);
            
            for(int i = 0; i < array.size(); i++){
                answer[i] = array.get(i);
            }
        }
        
        return answer;
    }
}