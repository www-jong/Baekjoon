import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N=sc.nextInt();
        for(int i=0;i<(N-1);i++){
            System.out.println(" ".repeat(N-1-i)+("*".repeat(i))+"*"+("*".repeat(i)));
        }
        System.out.println("**".repeat(N-1)+"*");
        for(int i=(N-2);i>=0;i--){
            System.out.println(" ".repeat(N-1-i)+("*".repeat(i))+"*"+("*".repeat(i)));
        }
        
    }
}