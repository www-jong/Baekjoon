import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int a=-1;
        int b=-1;
        int c=0;
        while(true){
            c=0;
            a=sc.nextInt();
            b=sc.nextInt();
            if(a==0&&b==0){
                break;
            }
            for(int i=1;i<=5000;i++){
                if(b==a*i){
                    System.out.println("factor");
                    c=1;      
                    break;
                }
            }
            if(c==0){
                if(a%b==0){
                    System.out.println("multiple");
                    c=1;
                }
            }
            if(c==0){
                System.out.println("neither");
            }
        }
    }
}