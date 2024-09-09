import java.util.ArrayList; 

class Solution {
    public ArrayList<Integer> solution(int[] num_list, int n) {
        ArrayList<Integer> list = new ArrayList<>();
        
//         i++는 1개씩 늘어나는 것. i+=2는 2개씩 늘어나는 것. 
//         i+=n은 n개씩 늘어나는 것. 
        for(int i = 0; i < num_list.length; i += n){
            list.add(num_list[i]);
        }
        
        return list;
    }
}