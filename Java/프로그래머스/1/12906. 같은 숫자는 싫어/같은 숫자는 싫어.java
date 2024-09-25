import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        /*
        for문을 돌면서 각 인덱스의 숫자 확인 
        이전 숫자와 다음 인덱스 숫자를 비교해서 
        다를 경우에만 list에 추가
            마지막 숫자 처리하기 
        */
        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < arr.length-1; i++){
            if(arr[i] != arr[i+1]){
                list.add(arr[i]);
            }
        }
        //마지막 숫자 처리 
        list.add(arr[arr.length-1]);

        
        int[] answer = new int[list.size()];
        int index = 0; 
        for(int num : list){
            answer[index++] = num;
        }
        

        return answer;
    }
}