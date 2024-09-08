import java.util.ArrayList;

class Solution {
     public ArrayList<Integer> solution(int n, int[] numlist) {
//          저장할 배열 리스트 생성 
        ArrayList<Integer> array = new ArrayList<>();

        for(int i = 0; i < numlist.length; i++){
            if(numlist[i] % n == 0){
//                 배수만 배열에 저장
                array.add(numlist[i]);
            }
        }

        return array;
    }
}