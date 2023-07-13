import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int h = sc.nextInt();
        int m = sc.nextInt();
        int tmp= h*60+m;
        if(tmp<45){
            tmp+=1440-45;
            System.out.printf("%d %d",tmp/60,tmp%60);
        }else{
            tmp-=45;
            System.out.printf("%d %d",tmp/60,tmp%60);    
        }
    }
}