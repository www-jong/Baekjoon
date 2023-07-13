import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        if(a>b){
            System.out.println(">");
        }
        else if(b>a){
            System.out.println("<");
        }
        else{
            System.out.println("==");
        }
    }
}