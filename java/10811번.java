import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] res= new int[N+1];
        for(int i=0;i<=N;i++){
            res[i]=i;
        }
        for(int i=0;i<M;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            int[] tmp=new int[b-a+2];
            for(int j=1;j<=(b-a+1);j++){
                tmp[j]=res[b-j+1];
            }
            for(int j=1;j<=(b-a+1);j++){
                res[a+j-1]=tmp[j];
            }
        }
        for(int i=1;i<=N;i++){
            System.out.print(res[i]+" ");
        }
    }
}