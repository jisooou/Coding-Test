class Solution {
    public String solution(int num) {
        String answer = "";
        
        if(num % 2 == 0){
            answer = "Even";
        }
//         num은 int 범위의 정수이다. 즉, 음수도 생각해야 한다. 
//         -1 % 2 == -1이다. 
        else if(num % 2 == 1 || num % 2 == -1){
            answer = "Odd";
        }

        return answer;
    }
}