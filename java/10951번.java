import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        while(sc.hasNext()){
            int A=sc.nextInt();
            int B=sc.nextInt();
            System.out.println(A+B);
        }
    sc.close();
    }
}