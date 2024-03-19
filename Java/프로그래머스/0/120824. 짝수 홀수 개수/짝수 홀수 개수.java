class Solution {
    public int[] solution(int[] num_list) {
        //odd와 even 2개를 받을 수 있는 배열 생성
        int[] answer = new int[2];
        int even = 0; 
        int odd = 0; 
        
        //배열을 도는 동안
        //만약에 배열의 인덱스 값이 2로 나눠 떨어지면 짝수이니까
        //짝수 ++ (홀수도 동일)
        for(int i = 0; i < num_list.length; i++){
            if(num_list[i] % 2 == 0){
                even++; 
            }
            else{
                odd++;
            }
        }
        
        answer[0] = even;
        answer[1] = odd;
        
        return answer;
    }
}