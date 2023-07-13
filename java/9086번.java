import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T= sc.nextInt();
        sc.nextLine();
        for(int i=0;i<T;i++){
        String A = sc.nextLine();
        System.out.print(A.charAt(0));
        System.out.println(A.charAt(A.length()-1));
        }
    }
}