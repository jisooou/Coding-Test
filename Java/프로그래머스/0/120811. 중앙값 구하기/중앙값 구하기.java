class Solution {
    public int solution(int[] array) {
        int answer = 0;
        
        for(int i = 0; i < array.length; i++){
            for(int j = i; j < array.length; j++){
                
                if(array[i] > array[j]){
                    int temp = array[i];
                    array[i] = array[j];
                    array[j] = temp; 
                    
                }
            }
            System.out.println(array[i]);
        }
        
        
        answer = array[(array.length / 2)];
        
        
        return answer;
    }
}