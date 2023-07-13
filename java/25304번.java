import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();
        int tmp = 0;
        int N = sc.nextInt();
        for(int i=0;i<N;i++){
            int a=sc.nextInt();
            int b=sc.nextInt();
            tmp+=a*b;
        }
        System.out.println((X==tmp)?"Yes":"No");
    }
}