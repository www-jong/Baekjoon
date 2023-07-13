import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] res=new int[30];
        for(int i=0;i<30;i++){
            res[i]=0;
        }
        for(int i=0;i<28;i++){
            int tmp=sc.nextInt();
            res[tmp-1]=1;
        }
        for(int i=0;i<30;i++){
            if(res[i]==0){
                System.out.println(i+1);
            }
        }
        
    }
}