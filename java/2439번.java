import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i=1;i<=T;i++){
            for(int j=T-i;j>0;j--){
                System.out.print(" ");
            }
            for(int j=1;j<=i;j++){
            System.out.print("*");
            }
            System.out.println();
        }
    }
}