class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        /*
        1. absolutes와 signs를 도는 동안에
        2. true이면 + 
        3. false이면 - 
        4. 계산한 값 리턴 
        */
        
        int sum = 0; 
        
        for(int i = 0; i < absolutes.length; i++){
            if(signs[i] == true){
                sum = sum + absolutes[i];
            }
            else{
                sum = sum - absolutes[i];
            }
            
        }
        
        return sum; 
    }
}