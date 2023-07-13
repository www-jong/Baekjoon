import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] tmp={1,1,2,2,2,8};
        String[] s=sc.nextLine().split(" ");
        
        for(int i=0;i<6;i++){
            System.out.print((tmp[i]-Integer.parseInt(s[i]))+" ");
        }
        
    }
}