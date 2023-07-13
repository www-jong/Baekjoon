import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] li = new int[N];
        int M=-1;
        for(int i=0;i<N;i++){
            int tmp = sc.nextInt();
            li[i]=tmp;
            if(M<tmp){
                M=tmp;
            }
        }
        int res=0;
        for(int i=0;i<N;i++){
            res+=li[i];
        }
        
        System.out.println(res/(double)M*100.0/N);
    }
}