import java.util.ArrayList; 

class Solution {
    public ArrayList<Integer> solution(int[] num_list) {
        // int[] answer = {};
        
        ArrayList<Integer> list = new ArrayList<>();
        
//         ArrayList에 일반적인 list를 넣기 위해서는 향상된 for문 사용
//         기존 num_list 배열에 있던 원소들을 ArrayList 안에 삽입
        for(int num : num_list){
            list.add(num);
        }
        
        
        if(num_list[num_list.length-1] > num_list[num_list.length-2]){
            int last = num_list[num_list.length-1] - num_list[num_list.length-2];
//             ArrayList 안에 (마지막 원소 - 그전 원소) 값 넣음
            list.add(last);
        }
        
//         크지 않다면 > 테스트케이스12 
        if(num_list[num_list.length-1] <= num_list[num_list.length-2]){
            int last = (num_list[num_list.length-1])*2;
//             ArrayList 안에 (마지막 원소 * 2) 값 넣음
            list.add(last);
        }
        
        
        
        return list;
    }
}