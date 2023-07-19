import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        int[] li=new int[n];
        int res = 0;
        for(int i=0;i<n;i++){
            li[i]=sc.nextInt();
        }
        boolean prime[] = new boolean[1002];
        prime[0]=prime[1]=true;
        for(int i=2;i*i<=1001;i++){
            if(!prime[i]){
                for(int j=i*i;j<=1001;j+=i){
                    prime[j]=true;
                }
            }
        }
        for(int i=0;i<n;i++){
            if(!prime[li[i]]){
                res+=1;
            }
        }
        System.out.println(res);
    }
}