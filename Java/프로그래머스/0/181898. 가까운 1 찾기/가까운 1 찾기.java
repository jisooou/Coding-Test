class Solution {
    public int solution(int[] arr, int idx) {
        
        //idx부터 for문을 돌면 된다
       for(int i = idx; i < arr.length; i++){
           
           if(arr[i] == 1){
               return i; 
           }
       }
        
        return -1;
    }
}