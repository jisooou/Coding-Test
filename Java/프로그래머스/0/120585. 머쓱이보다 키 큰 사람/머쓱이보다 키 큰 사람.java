class Solution {
    public int solution(int[] array, int height) {
        int answer = 0;
        for(int i = 0; i < array.length; i++){ 
            //만약에 array가 4칸이라고 가정 하에, 0부터 3까지 돌아야 함. 
            //0부터 4까지면 bound(범위)를 넘어섰기 때문에 오류 남. 
            if(array[i] > height){
                answer++;
            }
        }
        return answer;
    }
}