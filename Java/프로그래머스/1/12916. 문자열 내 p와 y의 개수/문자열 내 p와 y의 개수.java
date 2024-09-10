//배열 만들기 > toCharArray()

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        boolean error = false;
        int countP = 0;
        int countY = 0;

        //제한사항
        if(s.length() > 50){
            System.out.println("50이하의 자연수");
        }
        
        char[] array = s.toCharArray();
        
        for(int i = 0; i < array.length; i++){
            
            if(array[i] == 'p' || array[i] == 'P'){
                countP++;
            }
            
            if(array[i] == 'y' || array[i] == 'Y'){
                countY++;
            }
        }
        
        if(countP == countY){
            return answer; 
        }
        else if(countP != countY){
            return error; 
        }
        else{
            return answer;
        }
       
    }
}