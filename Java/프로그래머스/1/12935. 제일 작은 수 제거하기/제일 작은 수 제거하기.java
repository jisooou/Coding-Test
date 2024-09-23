class Solution {
    public int[] solution(int[] arr) {
        /*
        1. arr에 요소가 1개일 때는 -1을 리턴
        2. arr을 도는 동안 제일 작은 수 구하기 ( arr[i] < min , min == arr[i] )
        3. arr에서 제일 작은 수 빼기  
        */ 
        
        //arr 배열의 길이가 1이면 -1을 리턴
        if(arr.length == 1){
            int[] answer = {-1};
            return answer;
        } 
        
        int[] answer = new int[arr.length - 1]; 
        //제일 작은 수 min 구하기 
        int min = arr[0];
        for(int i = 0; i < arr.length; i++){
            if(arr[i] < min){
                min = arr[i];
            }
        }
        
        int index = 0;
        for(int i = 0; i < arr.length; i++){
            //배열 사이에 작은수가 껴있는 경우            
            if(arr[i] != min){
                answer[index++] = arr[i];
            }
        }
        
        return answer;
    }
}