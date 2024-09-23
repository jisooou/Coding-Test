class Solution {
    public int solution(String t, String p) {
        /*
        1. p의 문자열 길이를 구한다. 
        2. t에서 해당 문자열 길이만큼 돈다.
        3. t를 도는동안 나온 문자열들 중에서 
        4. p보다 작거나 같은 개수를 센다. (문자열 > 정수)
        */
        int count = 0;
        int pLength = p.length();
        String compare = "";
        
        //예) 0 ~ (7-3)4 > 0,1,2,3,4 
        for(int i = 0; i <= t.length() - pLength; i++){
            //예) substring(0, (0+3)3) > 314 
            compare = t.substring(i, i + pLength);
            //compare이 문자열이므로 정수로 변경 
            if(Long.parseLong(compare) <= Long.parseLong(p)){
                count++; 
            }
        }
        
        return count;
    }
}