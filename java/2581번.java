import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        sc.nextLine();
        int N= sc.nextInt();

        boolean prime[]=new boolean[N+2];
        prime[0]=prime[1]=true;
        for(int i=2;i<=N;i++){
            if(!prime[i]){
                for(int j=i*i;j<=N;j+=i){
                    prime[j]=true;
                }
            }
        }
        int sums= 0;
        int mins= 10000;
        for(int i=M;i<=N;i++){
            if(!prime[i]){
                sums+=i;
                if(mins==10000){
                    mins=i;
                }
            }
        }
    if(mins!=10000){
        System.out.println(sums);
        System.out.println(mins);
    }else{
        System.out.println(-1);
    }
    }
}