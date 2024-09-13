import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        /*
        Map을 사용
        */
        int answer = 0;
        int count = 0;
        
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num : tangerine){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        ArrayList<Integer> list = new ArrayList<>(map.values());
        //내림차순으로 정렬 
        Collections.sort(list, Collections.reverseOrder());
        
        int sum = 0;
        for(int a : list){
        //list에 있는 값에서 
            sum = sum + a; 
            count++;
            if(sum >= k){
                break;
                
            }

        }
        
        return count;
    }
}