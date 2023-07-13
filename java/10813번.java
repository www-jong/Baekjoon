import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] res=new int[N];
        for(int i=0;i<N;i++){
            res[i]=i+1;
        }
        for(int i=0;i<M;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            int tmp=0;
            tmp=res[a-1];
            res[a-1]=res[b-1];
            res[b-1]=tmp;
            
        }
        for(int i=0;i<N;i++){
            System.out.print(res[i]+" ");
        }
    }
}