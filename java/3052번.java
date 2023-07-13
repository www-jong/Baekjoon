import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        HashSet<Integer> res=new HashSet<Integer>();
        
        for(int i=0;i<10;i++){
            int tmp=sc.nextInt();
            res.add(tmp%42);
        }
        System.out.println(res.size());

    }
}