class Solution {
    public int[] solution(int[] arr) {
        /*
        1. arr에 요소가 1개일 때는 -1을 리턴
        2. arr을 도는 동안 제일 작은 수 구하기 ( arr[i] < min , min == arr[i] )
        3. arr 중 제일 작은 수가 아닐 경우, answer의 index를 하나씩 올려주고
        4. arr[i]의 값을 answer의 인덱스에 넣어준다. 
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
            //min이 아닐 경우, answer에 값을 넣어준다. 
            if(arr[i] != min){
                answer[index++] = arr[i];
            }
        }
        
        return answer;
    }
}