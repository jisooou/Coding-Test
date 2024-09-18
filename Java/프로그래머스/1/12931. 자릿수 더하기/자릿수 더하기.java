import java.util.*;

public class Solution {
    public int solution(int N) {
        //N을 하나씩 쪼개서 연산해도 되지만 
        //여기에서는 10으로 %, / 통해 계산 
        int sum = 0;

        while(N > 0){
            sum = sum + (N%10);
            N = N / 10;
        }

        return sum;
    }
}