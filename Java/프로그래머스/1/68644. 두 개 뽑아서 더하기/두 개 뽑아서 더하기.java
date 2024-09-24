import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        /*
            *for문을 2번 돌려서 합 구하기
            *중복 없애기
        */
        Set<Integer> set = new HashSet<>();
        
        for(int i = 0; i < numbers.length; i++){
            for(int j = i+1; j < numbers.length; j++){
                set.add(numbers[i] + numbers[j]);
            }
        }
        
        int[] answer = new int[set.size()];
        int index = 0; 
        for(int num : set){
            answer[index++] = num; 
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}