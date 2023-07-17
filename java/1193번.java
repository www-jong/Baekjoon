import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
		int idx = 0;
        int res = 1;
        while(res<=N){
            res+=idx;
            idx+=1;   
        }
        if(idx%2==1){
        System.out.println((N-(res-idx))+"/"+(res-N));
        }else{
        System.out.println((res-N)+"/"+(N-(res-idx)));
        }
    }
}