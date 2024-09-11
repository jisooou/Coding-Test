class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        boolean error = false;
        int sum = 0;
        
        String[] num = Integer.toString(x).split("");
        
        for(int i = 0; i < num.length; i++){
            sum = sum + Integer.parseInt(num[i]);
        }
        
        if(x % sum == 0){
            return answer; 
        }
        return error;
    }
    
}