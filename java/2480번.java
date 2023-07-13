import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
    if(A==B&&B==C){
        System.out.println(10000+A*1000);
    }else if(A==B||B==C||A==C){
        if(A==B){
            System.out.println(1000+A*100);
        }else if(B==C){
            System.out.println(1000+B*100);
        }else{
            System.out.println(1000+C*100);
        }
    }else{
        int max_val=(A>B)?((A>C)?A:C):(B>C)?B:C;
        System.out.println(max_val*100);
    }
    }
}