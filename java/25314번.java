import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        for(int i=0;i<(A/4);i++){
            System.out.print("long ");
        }
        System.out.println("int");
    }
}