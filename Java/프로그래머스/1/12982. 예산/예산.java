import java.util.*;
class Solution {
    public int solution(int[] d, int budget) {
        /*
        1.d를 돌면서 i들의 합이 9를 초과하기 전까지 count를 해준다. 
        2.count 값을 리턴한다.
        이때 배열 d는 오름차순정렬을 해줘야, 최대를 구할 수 있다. 
        */
        
        Arrays.sort(d);
        
        int sum = 0;
        int count = 0; 
        
        for(int i = 0; i < d.length; i++){
            sum = sum + d[i]; 
            
            if(sum > budget){
                return count; 
            }
            count++;
        }

        return count;
    }
}