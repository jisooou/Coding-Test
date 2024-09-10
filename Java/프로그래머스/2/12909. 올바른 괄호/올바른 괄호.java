class Solution {
    boolean solution(String s) {
        boolean answer = true;
        boolean error = false;
        int count = 0;
        
        char[] array = s.toCharArray();
        
        for(int i = 0; i < array.length; i++){
            
            if(array[i] == '('){
                count++;
            }
            else if(array[i] == ')'){
                count--;
                if(count < 0){
                    return error;
                }
            }
        }
        
        if(count == 0){
            return answer; 
        }
        else{
            return error;
        }
          
    }
}