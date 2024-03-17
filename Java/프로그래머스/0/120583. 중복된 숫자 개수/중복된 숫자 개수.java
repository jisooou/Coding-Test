class Solution {
    public int solution(int[] array, int n) {
        int answer = 0;
        for(int num : array){ //향상된 for문 사용하기 
            if(num == n){ //만약 array안에 num과 매개변수 n이 같으면 
                answer++;
            }
        }
        return answer;
    }
} 