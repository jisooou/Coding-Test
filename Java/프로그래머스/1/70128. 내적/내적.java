class Solution {
    public int solution(int[] a, int[] b) {
        /*
        배열 a와 배열 b의 길이가 같으므로 for문 1번만 돌려도O
        */
        int sum = 0; 
        
        for(int i = 0; i < a.length; i++){
            sum = sum + (a[i] * b[i]);
        }
         
        return sum;
    }
}