//x를 10,100,1000으로 나누면 몫+나머지 = x의각자릿수합 
class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        boolean error = false;
        
        int a = x / 10; 
        int b = x % 10;
        int c = x / 100;
        int d = x % 100; 
        int e = x / 1000; 
        int f = x % 1000; 
        
        //1~99
        if(x >= 1 && x <= 99){
            if(x % (a+b) == 0){
                return answer; 
            }
        }
        //101~999
        else if(x > 100 && x <= 999){
            if(x % (c + (d/10) + (d%10)) == 0){
                return answer; 
            }
        }
        //1001~9999
        else if(x > 1000 && x <= 9999){
            if(x % (e + (f/100) + ((f%100)/10) + ((f %100)%10)) == 0 ){
                return answer; 
            }
        }
        else if(x == 100 || x == 1000 || x == 10000){
            return answer; 
        }
        

        return error;
    }
}