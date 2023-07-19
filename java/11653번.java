import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N =sc.nextInt();
        int s = 2;
        while(N!=1){
            if(N%s==0){
                N=N/s;
                System.out.println(s);
            }else{
                s+=1;
            }
        }
    }
}