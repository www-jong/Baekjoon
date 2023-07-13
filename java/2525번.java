import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        int tmp = (A*60+B+C)%1440;
        System.out.printf("%d %d",tmp/60,tmp%60);
    }
}