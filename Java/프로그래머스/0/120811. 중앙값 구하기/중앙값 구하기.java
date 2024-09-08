// 오름차순 정렬에 해당하는 import
import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
       
        Arrays.sort(array);
        
        int mid = Math.round(array.length / 2);
    
        int answer = array[mid];
        
        return answer;
    }
}