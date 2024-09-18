class Solution {
    public int[] solution(Long n) {
        // 숫자 n을 문자열로 변환한 후, 길이를 구하여 len에 저장
        int len = Long.toString(n).length();
        
        // 결과를 저장할 배열을 길이 len만큼 생성
        int[] result = new int[len];
        
        // 숫자의 각 자리수를 배열에 저장
        for (int i = 0; i < len; i++) {
            // 현재 자리수의 숫자를 result 배열에 저장
            result[i] = (int) (n % 10);
            // n을 10으로 나누어 다음 자리수로 이동
            n /= 10;
        }
        
        // 결과 배열 반환
        return result;
    }
}