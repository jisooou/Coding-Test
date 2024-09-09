import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int[] array) {
        ArrayList<Integer> list = new ArrayList<>();
        
//         가장 큰 수 구하기 
        int max = Integer.MIN_VALUE; 
//         가장 큰 수의 인덱스 
        int maxIndex = Integer.MIN_VALUE;
        
        for(int i = 0; i < array.length; i++){
            if(array[i] > max){
                max = array[i];
//                 가장 큰 수의 인덱스 찾기
                maxIndex = i;
            } 
        }
        list.add(max);
        list.add(maxIndex);
        
        return list;
    }
}