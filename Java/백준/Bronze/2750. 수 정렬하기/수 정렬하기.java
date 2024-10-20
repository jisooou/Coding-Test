import java.io.BufferedReader; 
import java.io.InputStreamReader; 
import java.io.IOException; 

public class Main{
    public static void main(String[] args) throws IOException{
        //정렬 과정이 따로 없기 때문에 속도가 빠르다
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int N = Integer.parseInt(br.readLine());
        
        //절댓값이 1000 > -1000~1000 > 2001개(0포함)
        boolean[] arr = new boolean[2001];
        for(int i = 0; i < N; i++){
            //예) -1000 + 1000 = 0 > a[0] : 음수를 양수로 변환시켜주기 위해 +1000
            arr[Integer.parseInt(br.readLine()) + 1000] = true; 
        }
        
        for(int i = 0; i < 2001; i++){
            if(arr[i]){
                sb.append(i - 1000).append('\n');
            }
        }
        System.out.println(sb);
    }
}